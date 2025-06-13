with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Étude Op. 10 No. 11 in E♭ major\t')
    with Identification():
        Creator('Frédéric Chopin ', type='composer')
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
        CreditWords('Étude Op. 10 No. 11 in E♭ major ', default_x=841.641, default_y=2324.95, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('"Arpeggio"', default_x=841.641, default_y=2268.26, justify='center', valign='top', font_style='italic', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Frédéric Chopin ', default_x=1626.59, default_y=2224.95, justify='right', valign='bottom', font_size='12')
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
        with Measure(number='0', implicit='yes', width=154.23):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(182.2)
                with StaffLayout(number=2):
                    StaffDistance(86.02)
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(-3)
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
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegretto', default_x=-36.12, relative_y=55.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=76.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-36.12, relative_x=115.0, relative_y=55.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.12, default_y=-84.2, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('52')
                Staff(1)
                Sound(tempo=52.0)
            with Note(default_x=121.55, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='1', width=315.46):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-84.2, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=70.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=70.16, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=70.16, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=125.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=113.71, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=125.58, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=172.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=172.65, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=172.65, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=219.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=219.72, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=219.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=266.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=266.79, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=266.79, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-161.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=70.16, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=70.16, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=70.16, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.58, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.58, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.58, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=172.65, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=172.65, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=172.65, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=219.72, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=219.72, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=219.72, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=266.79, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=266.79, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=266.79, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='2', width=386.29):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=80.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=68.71, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=80.58, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=150.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=138.93, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=150.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=212.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=200.35, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=212.22, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=269.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=269.71, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=269.71, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=327.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=315.33, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=327.2, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=80.58, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=80.58, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=80.58, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=150.8, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=150.8, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=150.8, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=212.22, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=212.22, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=212.22, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=269.71, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=269.71, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=269.71, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=327.2, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=327.2, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=327.2, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='3', width=307.79):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=70.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=70.27, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=70.27, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=70.27, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=117.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=164.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=164.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=164.64, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=211.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=211.82, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=211.82, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=259.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=259.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=259.0, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=70.27, default_y=-136.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=70.27, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=70.27, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=70.27, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=117.45, default_y=-131.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=117.45, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=164.64, default_y=-166.02):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=164.64, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=164.64, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=211.82, default_y=-161.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=211.82, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=211.82, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=259.0, default_y=-161.02):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=259.0, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=259.0, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='4', width=385.14):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=89.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=77.64, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=89.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=89.51, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=148.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=148.31, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=148.31, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=148.31, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=207.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=207.12, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=207.12, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=207.12, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=265.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=265.93, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=265.93, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=265.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=324.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=324.73, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=324.73, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=324.73, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=23.09, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=23.09, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=89.51, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=77.64, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=89.51, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=89.51, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=148.31, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=148.31, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=148.31, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=148.31, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=207.12, default_y=-151.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=207.12, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=207.12, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=207.12, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=265.93, default_y=-151.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=265.93, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=265.93, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=324.73, default_y=-151.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=324.73, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=324.73, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=324.73, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='5', width=406.21):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(91.02)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=104.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=152.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=152.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=152.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=211.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=199.45, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=211.31, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=259.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=259.23, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=259.23, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=308.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=308.78, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=308.78, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=356.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=356.69, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=356.69, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.49)
                Staff(2)
            with Note(default_x=104.18, default_y=-176.02):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=152.09, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=152.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=152.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=211.31, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=211.31, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=211.31, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=259.23, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=259.23, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=259.23, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=308.78, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=308.78, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=308.78, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=356.69, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=356.69, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=356.69, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='6', width=402.13):
            with Note(default_x=33.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=92.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=92.46, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=80.59, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=92.46, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=162.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=162.67, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=150.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=162.67, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=224.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=224.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=212.23, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=224.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=282.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=282.91, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=282.91, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=282.91, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=341.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=341.72, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=329.85, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=341.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.49)
                Staff(2)
            with Note(default_x=33.64, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=21.78, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=92.46, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=80.59, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=92.46, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=92.46, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=162.67, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=150.81, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=162.67, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=162.67, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.09, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=212.23, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.09, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=282.91, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=271.04, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=282.91, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=282.91, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=341.72, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=329.85, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=341.72, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=341.72, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='7', width=361.44):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=107.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=107.18, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=107.18, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=107.18, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=154.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=154.99, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=143.13, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=154.99, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=216.41, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=216.41, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=204.55, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=216.41, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=264.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=264.22, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=264.22, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=312.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=312.03, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=312.03, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=107.18, default_y=-196.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=107.18, default_y=-186.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=107.18, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=107.18, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=154.99, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=154.99, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=154.99, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=216.41, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=216.41, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=216.41, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=264.22, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=264.22, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=264.22, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=312.03, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=312.03, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=312.03, default_y=-156.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
        with Measure(number='8', width=379.13):
            with Note(default_x=23.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=76.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=76.46, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=76.46, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=129.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=129.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=129.84, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=212.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-34.48, default_y=30.51)
            with Note(default_x=212.42, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=30.51)
            with Note(default_x=212.42, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=30.51)
            with Note(default_x=265.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=265.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=265.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=324.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=324.15, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=324.15, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-171.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.49)
            with Note(default_x=23.09, default_y=-161.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.49)
            with Note(default_x=76.46, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=76.46, default_y=-161.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=76.46, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=129.84, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=129.84, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=129.84, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=212.42, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=35.51)
            with Note(default_x=212.42, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=35.51)
            with Note(default_x=212.42, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=35.51)
            with Note(default_x=265.8, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=265.8, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=265.8, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=324.15, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=20.51)
            with Note(default_x=324.15, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=20.51)
            with Note(default_x=324.15, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=20.51)
            with Note(default_x=324.15, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=20.51)
        with Measure(number='9', width=407.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(88.03)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.3, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=104.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=104.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=104.18, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=154.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=154.53, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=154.53, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=204.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=15.51)
            with Note(default_x=204.88, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=15.51)
            with Note(default_x=204.88, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=15.51)
            with Note(default_x=255.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=255.23, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=255.23, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=305.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=305.58, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=305.58, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=355.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=355.93, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=355.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=104.18, default_y=-178.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=154.53, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=154.53, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=154.53, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=204.88, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=204.88, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=204.88, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=255.23, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=255.23, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=255.23, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=305.58, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=305.58, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=305.58, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=355.93, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=355.93, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=355.93, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='10', width=406.89):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=85.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=73.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=85.48, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=155.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=143.84, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=155.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=218.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=206.23, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=218.1, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=280.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=280.5, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=280.5, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=342.89, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=331.03, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=342.89, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=85.48, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=85.48, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=85.48, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=155.7, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=155.7, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=155.7, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=218.1, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=218.1, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=218.1, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=280.5, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=280.5, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=280.5, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=342.89, default_y=-148.03):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=342.89, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=342.89, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='11', width=328.39):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=73.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=73.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=73.7, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=73.7, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=124.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=174.94, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=174.94, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=174.94, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=225.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=225.56, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=225.56, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=276.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=276.17, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=276.17, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-143.03):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=73.7, default_y=-138.03):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=73.7, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=73.7, default_y=-113.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=73.7, default_y=-93.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=124.32, default_y=-133.03):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=-108.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=124.32, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=174.94, default_y=-168.03):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=174.94, default_y=-143.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=174.94, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=225.56, default_y=-163.03):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=225.56, default_y=-143.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=225.56, default_y=-118.03):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=276.17, default_y=-163.03):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=276.17, default_y=-138.03):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=276.17, default_y=-108.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='12', width=405.74):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=89.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=77.64, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=89.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=89.51, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=152.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=152.43, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=152.43, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=152.43, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.05)
                Staff(1)
            with Note(default_x=215.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=215.36, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=215.36, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=215.36, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-82.5)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-82.5)
                Staff(1)
            with Note(default_x=278.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=278.29, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=278.29, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=278.29, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=341.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=341.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=341.22, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=341.22, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-158.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=23.09, default_y=-133.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=23.09, default_y=-108.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=89.51, default_y=-158.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=77.64, default_y=-133.03):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=89.51, default_y=-128.03):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=89.51, default_y=-108.03):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=152.43, default_y=-158.03):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=152.43, default_y=-138.03):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=152.43, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=152.43, default_y=-113.03):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=215.36, default_y=-153.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=215.36, default_y=-133.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=215.36, default_y=-123.03):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=215.36, default_y=-108.03):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=278.29, default_y=-153.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=278.29, default_y=-128.03):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=278.29, default_y=-103.03):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=341.22, default_y=-153.03):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=341.22, default_y=-133.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=341.22, default_y=-118.03):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=341.22, default_y=-98.03):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='13', width=396.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(91.02)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=104.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=149.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.79, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=209.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=197.14, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=209.0, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=254.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=254.61, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=254.61, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=304.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=304.17, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=304.17, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=349.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=349.77, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=349.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.49)
                Staff(2)
            with Note(default_x=104.18, default_y=-176.02):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.79, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=149.79, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=149.79, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=209.0, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=209.0, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=209.0, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=254.61, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=254.61, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=254.61, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=304.17, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=304.17, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=304.17, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=349.77, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=349.77, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=349.77, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='14', width=392.9):
            with Note(default_x=33.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=90.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=90.15, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=78.28, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=90.15, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=160.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=160.37, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=148.5, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=160.37, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=221.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=221.79, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=209.92, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=221.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=278.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=278.29, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=278.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=278.29, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=334.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=334.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=322.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=334.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.49)
                Staff(2)
            with Note(default_x=33.64, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=21.78, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=90.15, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=78.28, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=90.15, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=90.15, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=160.37, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=148.5, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=160.37, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=160.37, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=221.79, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=209.92, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=221.79, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=221.79, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=278.29, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=266.43, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=278.29, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=278.29, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=334.8, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=322.93, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=334.8, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=334.8, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=352.21):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=105.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.34, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.34, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.34, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=151.3, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=151.3, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=139.44, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=151.3, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=212.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=212.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=200.85, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=212.72, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=258.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=258.68, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=258.68, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=304.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=304.65, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=304.65, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=105.34, default_y=-196.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.34, default_y=-186.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.34, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.34, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=151.3, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=151.3, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=151.3, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=212.72, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=212.72, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=212.72, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=258.68, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=258.68, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=258.68, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=304.65, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=304.65, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=304.65, default_y=-156.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
        with Measure(number='16', width=406.81):
            with Note(default_x=23.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=108.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=108.98, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=108.98, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=167.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Note(default_x=167.9, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Note(default_x=167.9, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Note(default_x=228.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=228.45, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=228.45, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=287.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=287.37, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=287.37, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=346.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=346.29, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=346.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-171.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.49)
            with Note(default_x=23.09, default_y=-161.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-24.49)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=108.98, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=108.98, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=108.98, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=167.9, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=167.9, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=167.9, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=228.45, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=30.51)
            with Note(default_x=228.45, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=30.51)
            with Note(default_x=228.45, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=30.51)
            with Note(default_x=287.37, default_y=-136.02):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=287.37, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=287.37, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=346.29, default_y=-136.02):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=346.29, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=346.29, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
        with Measure(number='17', width=405.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(103.2)
            with Note(default_x=135.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=135.27, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=135.27, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=177.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=177.22, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=177.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=217.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=5.51)
            with Note(default_x=205.97, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=5.51)
            with Note(default_x=217.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=5.51)
            with Note(default_x=256.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=256.98, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=256.98, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=302.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=302.73, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=302.73, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=364.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-42.33, default_y=20.51)
            with Note(default_x=364.52, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-42.33, default_y=20.51)
            with Note(default_x=364.52, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-42.33, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=135.27, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=135.27, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=135.27, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=177.22, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=177.22, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=177.22, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=217.84, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=217.84, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=217.84, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=256.98, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=256.98, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=256.98, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=302.73, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=302.73, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=302.73, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=364.52, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=364.52, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=364.52, default_y=-128.2):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='18', width=275.09):
            with Note(default_x=41.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-37.53, default_y=20.51)
            with Note(default_x=41.89, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-37.53, default_y=20.51)
            with Note(default_x=41.89, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-37.53, default_y=20.51)
            with Note(default_x=77.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=77.21, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=77.21, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=116.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=116.96, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=116.96, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=152.29, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=152.29, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=152.29, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=202.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=202.84, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=202.84, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=30.51)
            with Note(default_x=238.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=238.17, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=238.17, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=41.89, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=41.89, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=41.89, default_y=-133.2):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=77.21, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=77.21, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=77.21, default_y=-133.2):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=116.96, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=116.96, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=116.96, default_y=-133.2):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=152.29, default_y=-178.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=152.29, default_y=-148.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=152.29, default_y=-133.2):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=202.84, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=202.84, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=202.84, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=238.17, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=238.17, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=238.17, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='19', width=291.8):
            with Note(default_x=33.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=33.09, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=33.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=69.82, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=69.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=69.82, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=121.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=10.51)
            with Note(default_x=109.57, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=10.51)
            with Note(default_x=121.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=10.51)
            with Note(default_x=158.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=158.16, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=158.16, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-83.8)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-83.8)
                Staff(1)
            with Note(default_x=203.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=203.92, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=203.92, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=253.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=253.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=253.47, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=33.09, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=33.09, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=33.09, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=69.82, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=69.82, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=69.82, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=121.44, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=121.44, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=121.44, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=158.16, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=158.16, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=158.16, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=203.92, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=30.51)
            with Note(default_x=203.92, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=30.51)
            with Note(default_x=203.92, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=30.51)
            with Note(default_x=253.47, default_y=-168.2):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.47, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.47, default_y=-123.2):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='20', width=271.81):
            with Note(default_x=33.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=33.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=68.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=68.49, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=68.49, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=118.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.29, default_y=15.51)
            with Note(default_x=118.25, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.29, default_y=15.51)
            with Note(default_x=118.25, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.29, default_y=15.51)
            with Note(default_x=153.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=153.65, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=153.65, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=199.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=199.4, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=199.4, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=234.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=234.81, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=234.81, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=33.09, default_y=-173.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=33.09, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=33.09, default_y=-128.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=68.49, default_y=-173.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=68.49, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=68.49, default_y=-128.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=118.25, default_y=-173.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=118.25, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=118.25, default_y=-128.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=153.65, default_y=-173.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=153.65, default_y=-143.2):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=153.65, default_y=-128.2):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=199.4, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=199.4, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=199.4, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=234.81, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=234.81, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=234.81, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='21', width=304.95):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.8, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-78.8)
                Staff(1)
            with Note(default_x=33.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=33.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=33.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=70.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=70.06, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=70.06, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=125.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=113.62, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=125.48, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=162.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=162.46, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=162.46, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=216.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=216.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=216.82, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=266.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=266.37, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=266.37, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('segue', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=33.09, default_y=-158.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=33.09, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=33.09, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=70.06, default_y=-158.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=70.06, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=70.06, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.48, default_y=-158.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.48, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=125.48, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=162.46, default_y=-158.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=162.46, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=162.46, default_y=-113.2):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=216.82, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=216.82, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=216.82, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=266.37, default_y=-163.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=266.37, default_y=-138.2):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=266.37, default_y=-118.2):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='22', width=394.04):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(89.35)
            with Note(default_x=135.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Note(default_x=135.27, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Note(default_x=135.27, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-83.65)
                Staff(1)
            with Note(default_x=177.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=177.22, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=177.22, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=10.51)
            with Note(default_x=228.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=5.51)
            with Note(default_x=216.97, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=5.51)
            with Note(default_x=228.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=5.51)
            with Note(default_x=266.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=266.86, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=266.86, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=304.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=304.87, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=304.87, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=354.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=354.42, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=354.42, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-81.44)
                Staff(2)
            with Note(default_x=135.27, default_y=-154.35):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=135.27, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=135.27, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=177.22, default_y=-154.35):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=177.22, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=177.22, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=228.84, default_y=-154.35):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=228.84, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=228.84, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=266.86, default_y=-154.35):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=266.86, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=266.86, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.4)
                Staff(2)
            with Note(default_x=304.87, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=304.87, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=304.87, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=354.42, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=354.42, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=354.42, default_y=-114.35):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='23', width=281.9):
            with Note(default_x=33.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=33.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=69.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=69.6, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=69.6, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-97.8)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-97.8)
                Staff(1)
            with Note(default_x=121.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=-4.49)
            with Note(default_x=109.35, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=-4.49)
            with Note(default_x=121.22, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=-4.49)
            with Note(default_x=157.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=157.72, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=157.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=207.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=5.51)
            with Note(default_x=207.28, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=5.51)
            with Note(default_x=207.28, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=5.51)
            with Note(default_x=243.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=243.79, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=243.79, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=33.09, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=33.09, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=33.09, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=69.6, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=69.6, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=69.6, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=121.22, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=121.22, default_y=-149.35):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=121.22, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=157.72, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=157.72, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=157.72, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=207.28, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=207.28, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=207.28, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=243.79, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=243.79, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=243.79, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='24', width=301.67):
            with Direction(placement='above'):
                with DirectionType():
                    Words('con forza', default_y=55.77, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=38.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=0.51)
            with Note(default_x=38.09, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=0.51)
            with Note(default_x=38.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=0.51)
            with Note(default_x=81.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note(default_x=81.64, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note(default_x=81.64, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=5.51)
            with Note(default_x=119.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=119.75, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=119.75, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=157.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=157.85, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=157.85, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=216.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=10.51)
            with Note(default_x=216.21, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=10.51)
            with Note(default_x=216.21, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=10.51)
            with Note(default_x=261.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=0.51)
            with Note(default_x=261.96, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=0.51)
            with Note(default_x=261.96, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=0.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=38.09, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=38.09, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=38.09, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=81.64, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=81.64, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=81.64, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=15.51)
            with Note(default_x=119.75, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=119.75, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=119.75, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=157.85, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=157.85, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=157.85, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=216.21, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=216.21, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=216.21, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.89, default_y=15.51)
            with Note(default_x=261.96, default_y=-164.35):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=15.51)
            with Note(default_x=261.96, default_y=-144.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=15.51)
            with Note(default_x=261.96, default_y=-119.35):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='25', width=278.24):
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-75.8, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('42')
                Staff(1)
                Sound(tempo=42.0)
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dolce', default_y=-42.2, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=-75.8, relative_y=-30.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Note(default_x=65.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=65.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=65.36, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=112.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=112.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=112.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=150.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.84, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.84, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.4)
                Staff(1)
            with Note(default_x=200.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=200.39, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=200.39, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=238.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=238.51, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=238.51, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=13.8, default_y=-194.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-159.35):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.0)
                Staff(2)
            with Note(default_x=65.36, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=65.36, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=65.36, default_y=-114.35):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=112.72, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=112.72, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=112.72, default_y=-114.35):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.84, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.84, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=150.84, default_y=-114.35):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=200.39, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=200.39, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=200.39, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=238.51, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=238.51, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=238.51, default_y=-104.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='26', width=293.06):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.4, relative_x=60.0, relative_y=-40.0):
                        Pp()
                        OtherDynamics(' poco ritenuto')
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.42, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note(default_x=33.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=33.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=33.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=34.63, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                Staff(1)
                Sound(tempo=69.0)
            with Note(default_x=82.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=82.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=82.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=36.84, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                Staff(1)
                Sound(tempo=66.0)
            with Note(default_x=129.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=129.99, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=129.99, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=36.84, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('63')
                Staff(1)
                Sound(tempo=63.0)
            with Note(default_x=168.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=168.03, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=168.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('57')
                Staff(1)
                Sound(tempo=57.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=20.13, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=215.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=215.39, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=215.39, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=253.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.42, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.42, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.0)
                Staff(2)
            with Note(default_x=33.09, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.0)
                Staff(2)
            with Note(default_x=82.64, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=82.64, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=82.64, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=129.99, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=129.99, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=129.99, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=168.03, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=168.03, default_y=-134.35):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=168.03, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.0)
                Staff(2)
            with Note(default_x=215.39, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=215.39, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=215.39, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.42, default_y=-159.35):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.42, default_y=-139.35):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=253.42, default_y=-109.35):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='27', width=491.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(129.12)
                with StaffLayout(number=2):
                    StaffDistance(76.02)
            with Note(default_x=104.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=104.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=32.11, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Note(default_x=162.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=162.11, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=162.11, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=220.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=220.03, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=220.03, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=277.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=277.96, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=277.96, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=335.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
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
                    Slur(type='start', placement='above', number=2)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=335.89, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=335.89, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=383.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=371.53, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=383.4, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=442.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
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
                    Slur(type='stop', number=2)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=442.78, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=442.78, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=104.18, default_y=-181.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=162.11, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=162.11, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=162.11, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=220.03, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=220.03, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=220.03, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=277.96, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=277.96, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=277.96, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=335.89, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=335.89, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=335.89, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=413.09, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=413.09, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=413.09, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='28', width=352.22):
            with Note(default_x=33.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=33.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=33.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_y=-40.0):
                        Pp()
                        OtherDynamics(' dolcissimo')
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=86.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=86.01, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=86.01, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=138.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=138.93, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=138.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=191.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=191.86, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=191.86, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=244.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=244.78, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=244.78, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=297.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=297.7, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=297.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=33.09, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=33.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=86.01, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=86.01, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=86.01, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=138.93, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=138.93, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=138.93, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=191.86, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=191.86, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=191.86, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=244.78, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=244.78, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=244.78, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=297.7, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=297.7, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=297.7, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='29', width=341.57):
            with Note(default_x=23.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=75.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=75.9, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=75.9, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=20.51)
            with Note(default_x=128.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=128.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=128.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=181.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=181.53, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=181.53, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=234.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=234.34, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=234.34, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=287.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=287.16, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=287.16, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=23.09, default_y=-181.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=75.9, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=75.9, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=75.9, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=128.72, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=128.72, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=128.72, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=15.51)
            with Note(default_x=181.53, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=181.53, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=181.53, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=234.34, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=234.34, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=234.34, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=287.16, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=287.16, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=287.16, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='30', width=363.22):
            with Note(default_x=44.09, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-41.09, default_y=25.51)
            with Note(default_x=44.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=25.51)
            with Note(default_x=44.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=25.51)
            with Note(default_x=97.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=97.01, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=97.01, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.93, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.93, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=202.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=202.86, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=202.86, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=255.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=255.78, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=255.78, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=308.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=308.7, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=308.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.49)
                Staff(2)
            with Note(default_x=44.09, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=44.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=44.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=97.01, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=97.01, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=97.01, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=149.93, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=149.93, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=149.93, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=202.86, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=202.86, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=202.86, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=255.78, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=255.78, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=255.78, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=308.7, default_y=-146.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=308.7, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=308.7, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='31', width=1548.91):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=137.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-36.69, default_y=25.51)
            with Note(default_x=137.07, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=25.51)
            with Note(default_x=137.07, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=25.51)
            with Note(default_x=372.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=372.11, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=372.11, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=607.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=607.15, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=607.15, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=842.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=842.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=842.19, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1077.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=1077.23, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=1077.23, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=1312.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1312.27, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1312.27, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.0)
                Staff(2)
            with Note(default_x=137.07, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=137.07, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=137.07, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=372.11, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=372.11, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=372.11, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=607.15, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=20.51)
            with Note(default_x=607.15, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=20.51)
            with Note(default_x=607.15, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=20.51)
            with Note(default_x=842.19, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=842.19, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=842.19, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1077.23, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=1077.23, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=1077.23, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=30.51)
            with Note(default_x=1312.27, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1312.27, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=1312.27, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='32', width=458.02):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(86.02)
            with Note(default_x=134.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=134.86, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=134.86, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Note(default_x=134.86, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=32.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=188.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=188.45, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=188.45, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=28.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                Staff(1)
                Sound(tempo=68.0)
            with Note(default_x=242.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=242.05, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=242.05, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('rit.', default_y=-40.0, relative_x=26.57, relative_y=-39.55, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                Staff(1)
                Sound(tempo=64.0)
            with Note(default_x=295.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=295.64, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=295.64, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-22.12)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=349.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=50.51)
            with Note(default_x=349.24, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=50.51)
            with Note(default_x=349.24, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=50.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=33.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('56')
                Staff(1)
                Sound(tempo=56.0)
            with Note(default_x=402.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=402.83, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=402.83, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=134.86, default_y=-151.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=134.86, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=134.86, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=134.86, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=188.45, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=188.45, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=188.45, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=188.45, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=242.05, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=242.05, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=242.05, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=242.05, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=295.64, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=295.64, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=295.64, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=295.64, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=349.24, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=349.24, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=349.24, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=349.24, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=402.83, default_y=-156.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=402.83, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=402.83, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=402.83, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='33', width=348.86):
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=31.79, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=76.0)
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=76.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=76.84, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=76.84, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=132.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=120.39, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=132.26, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-35.95, default_y=15.51)
            with Note(default_x=186.01, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=186.01, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=186.01, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=228.23, default_y=25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=239.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=239.76, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=239.76, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=293.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=293.51, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=293.51, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-176.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.84, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=76.84, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=76.84, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=132.26, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=132.26, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=132.26, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=186.01, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=186.01, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=186.01, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=239.76, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=239.76, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=239.76, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=293.51, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=293.51, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=293.51, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='34', width=419.69):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=88.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=76.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=88.04, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=158.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=146.4, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=158.26, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=15.51)
            with Note(default_x=223.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=211.35, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=223.22, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=20.51)
            with Note(default_x=276.64, default_y=25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=288.17, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=288.17, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=288.17, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51, relative_x=-10.0)
            with Note(default_x=353.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=341.27, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Note(default_x=353.13, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=88.04, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=88.04, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=88.04, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.26, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.26, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.26, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=223.22, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=223.22, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=223.22, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=288.17, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=288.17, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=288.17, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=353.13, default_y=-146.02):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=353.13, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=353.13, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='35', width=322.33):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=23.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=72.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=72.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=72.7, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=72.7, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=122.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=171.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=171.91, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Note(default_x=171.91, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=221.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=221.52, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=221.52, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=271.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=271.13, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=271.13, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-141.02):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=72.7, default_y=-136.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=72.7, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=72.7, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=72.7, default_y=-91.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=122.3, default_y=-131.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=122.3, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=171.91, default_y=-166.02):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=171.91, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Note(default_x=171.91, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=10.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=221.52, default_y=-161.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=221.52, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Note(default_x=221.52, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=15.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.5)
                Staff(2)
            with Note(default_x=271.13, default_y=-161.02):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=271.13, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=271.13, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='36', width=451.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(91.02)
            with Note(default_x=113.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=113.47, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=113.47, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=179.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=168.02, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=179.88, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=179.88, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=35.51)
            with Note(default_x=233.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=233.37, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=233.37, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=233.37, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=289.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=289.52, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=289.52, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=289.52, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=30.51)
            with Note(default_x=343.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=343.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=343.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=343.0, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=396.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=396.49, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=396.49, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=396.49, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=113.47, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=113.47, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=113.47, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=179.88, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=168.02, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=179.88, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Note(default_x=179.88, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-46.95, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=233.37, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=233.37, default_y=-141.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=233.37, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=233.37, default_y=-116.02):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=289.52, default_y=-156.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=289.52, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=289.52, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=289.52, default_y=-111.02):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=343.0, default_y=-156.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=343.0, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Note(default_x=343.0, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=396.49, default_y=-156.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=396.49, default_y=-136.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=396.49, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=396.49, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='37', width=334.28):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=69.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=69.2, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=69.2, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=128.41, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=116.55, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=128.41, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-39.75, default_y=20.51)
            with Note(default_x=174.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=174.52, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=174.52, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=211.94, default_y=30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=240.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=240.47, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=240.47, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=286.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=286.58, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=286.58, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=23.09, default_y=-176.02):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=69.2, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=69.2, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=69.2, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=128.41, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=128.41, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=128.41, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=174.52, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=174.52, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=174.52, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=240.47, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=240.47, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=240.47, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=286.58, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=286.58, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=286.58, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='38', width=411.3):
            with Note(default_x=33.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=33.64, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=93.13, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=93.13, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=81.27, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=93.13, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=163.35, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=163.35, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=151.49, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=163.35, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-50.75, default_y=20.51)
            with Note(default_x=224.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=224.77, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=212.9, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=224.77, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=25.51)
            with Note(default_x=259.69, default_y=30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=290.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=290.72, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=290.72, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=290.72, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=30.51, relative_x=-10.0)
            with Note(default_x=350.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=350.21, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=338.34, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Note(default_x=350.21, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=25.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=33.64, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=21.78, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=33.64, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.64, default_y=35.51)
            with Note(default_x=93.13, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=81.27, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=93.13, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=93.13, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=163.35, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=151.49, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=163.35, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=163.35, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.77, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=212.9, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.77, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=224.77, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=290.72, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=278.85, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=290.72, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=290.72, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=350.21, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=338.34, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=350.21, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Note(default_x=350.21, default_y=-101.02):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='39', width=351.75):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=23.09, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=50.51)
            with Note(default_x=105.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.25, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.25, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=105.25, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=151.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=151.12, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=139.25, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=151.12, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.95, default_y=40.51)
            with Note(default_x=212.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=212.54, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=200.67, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=212.54, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.95, default_y=40.51)
            with Note(default_x=258.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=258.41, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=258.41, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=304.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=304.28, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=304.28, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-131.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-96.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=105.25, default_y=-196.02):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.25, default_y=-186.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.25, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=105.25, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-14.49)
            with Note(default_x=151.12, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=151.12, default_y=-171.02):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=151.12, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=212.54, default_y=-191.02):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=212.54, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=212.54, default_y=-146.02):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=258.41, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=258.41, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=258.41, default_y=-151.02):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=304.28, default_y=-186.02):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=304.28, default_y=-166.02):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=304.28, default_y=-156.02):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
        with Measure(number='40', width=476.41):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=126.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Note(default_x=126.69, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Note(default_x=126.69, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Note(default_x=184.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=45.51)
            with Note(default_x=184.71, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=45.51)
            with Note(default_x=184.71, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=45.51)
            with Note(default_x=242.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=242.73, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=242.73, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=300.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=300.75, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=300.75, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=358.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=358.77, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=358.77, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=416.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Note(default_x=416.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Note(default_x=416.79, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=45.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=126.69, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-4.49)
            with Note(default_x=126.69, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-4.49)
            with Note(default_x=126.69, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-4.49)
            with Note(default_x=126.69, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-4.49)
            with Note(default_x=184.71, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=-9.49)
            with Note(default_x=184.71, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=-9.49)
            with Note(default_x=184.71, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=-9.49)
            with Note(default_x=184.71, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.32, default_y=-9.49)
            with Note(default_x=242.73, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=242.73, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=242.73, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=242.73, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-9.49)
            with Note(default_x=300.75, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-37.29, default_y=-4.49)
            with Note(default_x=300.75, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-37.29, default_y=-4.49)
            with Note(default_x=300.75, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-37.29, default_y=-4.49)
            with Note(default_x=300.75, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-37.29, default_y=-4.49)
            with Note(default_x=358.77, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=358.77, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=358.77, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=358.77, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=416.79, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=416.79, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=416.79, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=416.79, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
        with Measure(number='41', width=332.9):
            with Note(default_x=33.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=33.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=33.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=45.51)
            with Note(default_x=81.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=81.61, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=81.61, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=130.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=130.14, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=130.14, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=178.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=178.66, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=178.66, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=227.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=227.19, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=227.19, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=282.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=282.77, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=282.77, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=33.09, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=33.09, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=33.09, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=33.09, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=81.61, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=81.61, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=81.61, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=81.61, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=130.14, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=130.14, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=130.14, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=130.14, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-9.49)
            with Note(default_x=178.66, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-14.49)
            with Note(default_x=178.66, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-14.49)
            with Note(default_x=178.66, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-14.49)
            with Note(default_x=178.66, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-14.49)
            with Note(default_x=227.19, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=227.19, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=227.19, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=227.19, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=282.77, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=-14.49)
            with Note(default_x=282.77, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=-14.49)
            with Note(default_x=282.77, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=-14.49)
            with Note(default_x=282.77, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=-14.49)
        with Measure(number='42', width=400.66):
            with Note(default_x=41.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=35.51)
            with Note(default_x=41.32, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=35.51)
            with Note(default_x=41.32, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=35.51)
            with Note(default_x=98.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=35.51)
            with Note(default_x=98.76, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=35.51)
            with Note(default_x=98.76, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=35.51)
            with Note(default_x=156.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=156.19, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=156.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=221.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=35.51)
            with Note(default_x=221.75, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=35.51)
            with Note(default_x=221.75, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-41.09, default_y=35.51)
            with Note(default_x=279.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=279.18, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=279.18, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=336.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=336.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=336.62, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=41.32, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-38.32, default_y=-14.49)
            with Note(default_x=41.32, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.32, default_y=-14.49)
            with Note(default_x=41.32, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.32, default_y=-14.49)
            with Note(default_x=41.32, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-38.32, default_y=-14.49)
            with Note(default_x=98.76, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=-19.49)
            with Note(default_x=98.76, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=-19.49)
            with Note(default_x=98.76, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=-19.49)
            with Note(default_x=98.76, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=-19.49)
            with Note(default_x=156.19, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=156.19, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=156.19, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=156.19, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-19.49)
            with Note(default_x=221.75, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-49.89, default_y=-14.49)
            with Note(default_x=221.75, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-49.89, default_y=-14.49)
            with Note(default_x=221.75, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-49.89, default_y=-14.49)
            with Note(default_x=221.75, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-49.89, default_y=-14.49)
            with Note(default_x=279.18, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=279.18, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=279.18, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=279.18, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-14.49)
            with Note(default_x=336.62, default_y=-175.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-19.49)
            with Note(default_x=336.62, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-19.49)
            with Note(default_x=336.62, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-19.49)
            with Note(default_x=336.62, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=-19.49)
        with Measure(number='43', width=338.94):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=30.89, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=30.89, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=30.89, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=81.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=81.96, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=81.96, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=25.51)
            with Note(default_x=133.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-26.29, default_y=25.51)
            with Note(default_x=133.04, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=25.51)
            with Note(default_x=133.04, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=25.51)
            with Note(default_x=184.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=184.11, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=184.11, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=235.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=235.19, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=235.19, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=15.51)
            with Note(default_x=286.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=286.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=286.26, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Backup():
                Duration(36.0)
            with Note(default_x=30.89, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=30.89, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=30.89, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=30.89, default_y=-70.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=40.51)
            with Note(default_x=81.96, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=81.96, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=81.96, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-90.27)
                Staff(2)
            with Note(default_x=133.04, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=133.04, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=133.04, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=133.04, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=184.11, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=184.11, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=184.11, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=184.11, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=235.19, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=235.19, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=235.19, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=235.19, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=286.26, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=286.26, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=286.26, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=286.26, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='44', width=353.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(82.72)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=33.62, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('42')
                Staff(1)
                Sound(tempo=42.0)
            with Note(default_x=104.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=104.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=44.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Note(default_x=149.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=149.93, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=149.93, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=197.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=197.28, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=197.28, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=235.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=235.88, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=235.88, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=274.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=274.48, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=274.48, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=313.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=313.08, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=313.08, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=104.18, default_y=-172.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=149.93, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=149.93, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=197.28, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.28, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=197.28, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=235.88, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.88, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=235.88, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=274.48, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.48, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=274.48, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.08, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=313.08, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=313.08, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=313.08, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=154.23, default_y=-117.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Forward():
                Duration(6.0)
        with Measure(number='45', width=276.56):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=72.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=72.64, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=72.64, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=119.99, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=119.99, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=158.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=197.48, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=197.48, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=236.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=23.09, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=72.64, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=72.64, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=72.64, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=197.48, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='46', width=272.19):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.39, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('42')
                Staff(1)
                Sound(tempo=42.0)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=35.0, relative_x=-30.0)
                Staff(1)
            with Note(default_x=23.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=23.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=5.63)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=44.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=68.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=68.84, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=68.84, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=35.51)
            with Note(default_x=116.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=116.19, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=116.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=154.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=154.79, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=154.79, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=193.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=193.39, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=193.39, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=231.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=231.99, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=231.99, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=23.09, default_y=-172.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=68.84, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=68.84, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=116.19, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.19, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=116.19, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=154.79, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.79, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=154.79, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=193.39, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.39, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=193.39, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.99, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=231.99, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=231.99, default_y=-107.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=231.99, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(6.0)
            with Note(default_x=73.14, default_y=-117.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Forward():
                Duration(6.0)
        with Measure(number='47', width=276.56):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=72.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=72.64, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=72.64, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=119.99, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=119.99, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=35.51)
            with Note(default_x=158.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=197.48, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=197.48, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=236.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=23.09, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=23.09, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=72.64, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=72.64, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=72.64, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=119.99, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-112.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=158.74, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.49)
                Staff(2)
            with Note(default_x=197.48, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=197.48, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Note(default_x=236.22, default_y=-87.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=40.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='48', width=370.31):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=45.0)
                Staff(1)
            with Note(default_x=23.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=23.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=23.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.12, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-86.12)
                Staff(1)
            with Note(default_x=110.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=110.13, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=110.13, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=160.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=160.89, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=160.89, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.0)
                Staff(1)
            with Note(default_x=213.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=213.25, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=213.25, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=267.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=267.19, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=267.19, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=317.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=317.95, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=317.95, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-137.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-117.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-92.72):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=110.13, default_y=-182.72):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=110.13, default_y=-162.72):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=110.13, default_y=-137.72):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-26.29, default_y=-9.49)
            with Note(default_x=160.89, default_y=-187.72):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=160.89, default_y=-167.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=160.89, default_y=-157.72):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=160.89, default_y=-142.72):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=213.25, default_y=-172.72):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=213.25, default_y=-162.72):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=213.25, default_y=-142.72):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=267.19, default_y=-192.72):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=267.19, default_y=-172.72):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=267.19, default_y=-162.72):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=267.19, default_y=-147.72):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=317.95, default_y=-177.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=317.95, default_y=-157.72):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=317.95, default_y=-147.72):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=317.95, default_y=-132.72):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
        with Measure(number='49', width=420.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(77.3)
            with Note(default_x=111.89, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=111.89, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=111.89, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=167.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=167.26, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=167.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=25.51)
            with Note(default_x=214.96, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=214.96, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Note(default_x=214.96, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-27.89, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-78.2)
                Staff(1)
            with Note(default_x=267.32, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=267.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=267.32, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-32.32, default_y=25.51)
            with Note(default_x=321.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=321.26, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=321.26, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-34.48, default_y=25.51)
            with Note(default_x=370.81, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=370.81, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Note(default_x=370.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=20.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Note(default_x=111.89, default_y=-157.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=111.89, default_y=-147.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=111.89, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=167.26, default_y=-177.3):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=167.26, default_y=-157.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=167.26, default_y=-132.3):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-9.49)
            with Note(default_x=214.96, default_y=-182.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=214.96, default_y=-162.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=214.96, default_y=-152.3):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=214.96, default_y=-137.3):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-24.09, default_y=-14.49)
            with Note(default_x=267.32, default_y=-167.3):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=267.32, default_y=-157.3):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=267.32, default_y=-137.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.69, default_y=-14.49)
            with Note(default_x=321.26, default_y=-187.3):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=321.26, default_y=-167.3):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=321.26, default_y=-157.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=321.26, default_y=-142.3):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-35.09, default_y=-19.49)
            with Note(default_x=370.81, default_y=-172.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=370.81, default_y=-152.3):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=370.81, default_y=-142.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
            with Note(default_x=370.81, default_y=-127.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=-4.49)
        with Measure(number='50', width=277.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.2, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=22.73, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=22.73, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=22.73, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=195.4, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=252.25, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(36.0)
            with Forward():
                Duration(24.0)
            with Note(default_x=195.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-157.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=23.09, default_y=-137.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=23.09, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=5.6, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=40.6)
                Staff(2)
            with Note(default_x=58.07, default_y=-172.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=58.07, default_y=-147.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=58.07, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=113.66, default_y=-177.3):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=0.51)
            with Note(default_x=113.66, default_y=-152.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=0.51)
            with Note(default_x=113.66, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-39.92, default_y=0.51)
            with Note(default_x=148.64, default_y=-172.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=148.64, default_y=-147.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=148.64, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=195.4, default_y=-167.3):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-31.09, default_y=0.51)
            with Note(default_x=195.4, default_y=-142.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.09, default_y=0.51)
            with Note(default_x=195.4, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.09, default_y=0.51)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=6.0, relative_y=30.0):
                        F()
                Staff(2)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=39.95)
                Staff(2)
            with Note(default_x=230.38, default_y=-172.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=230.38, default_y=-142.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
            with Note(default_x=230.38, default_y=-127.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=-4.49)
        with Measure(number='51', width=345.02):
            with Note(default_x=23.09, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=239.03, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=279.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Tuplet(type='start', bracket='no')
            with Note(default_x=299.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.25, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(12.0)
            with Note(default_x=239.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-157.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=23.09, default_y=-147.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=23.09, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('smorz.', default_y=88.77, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.2, relative_y=-40.0):
                        Pp()
                Staff(2)
                Sound(dynamics=61.11)
            with Note(default_x=88.98, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=88.98, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=88.98, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=39.72)
                Staff(2)
            with Note(default_x=144.56, default_y=-152.3):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=25.51)
            with Note(default_x=144.56, default_y=-127.3):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=25.51)
            with Note(default_x=144.56, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-36.12, default_y=25.51)
            with Note(default_x=184.67, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=184.67, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=184.67, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=239.03, default_y=-142.3):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=239.03, default_y=-117.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Note(default_x=239.03, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-34.89, default_y=25.51)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=40.0)
                Staff(2)
            with Note(default_x=279.14, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=279.14, default_y=-117.3):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=279.14, default_y=-102.3):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
        with Measure(number='52', width=261.41):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=7.29, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('32')
                Staff(1)
                Sound(tempo=32.0)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.85, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Staff(1)
                Sound(tempo=76.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=2, default_y=-85.0)
                Staff(1)
            with Note(default_x=54.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=54.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=54.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=95.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=95.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=95.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=136.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=136.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=136.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=2, relative_x=-6.14)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-25.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=177.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=177.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=177.8, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=218.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=218.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Note(default_x=218.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=20.51)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.18)
                Staff(2)
            with Note(default_x=13.8, default_y=-167.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Note(default_x=54.8, default_y=-157.3):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=54.8, default_y=-132.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=54.8, default_y=-112.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=95.8, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=95.8, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=95.8, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=136.8, default_y=-132.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=136.8, default_y=-112.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=136.8, default_y=-87.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=177.8, default_y=-122.3):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=177.8, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=177.8, default_y=-77.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=45.51)
            with Note(default_x=218.8, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=218.8, default_y=-122.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
            with Note(default_x=218.8, default_y=-97.3):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.51)
        with Measure(number='53', width=135.57):
            with Note(default_x=23.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=10.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=65.12, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('40')
                Staff(1)
                Sound(tempo=40.0)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=69.32, relative_x=-29.49)
                Staff(1)
            with Note(default_x=78.56, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.56, default_y=-20.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=97.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Backup():
                Duration(36.0)
            with Note(default_x=23.09, default_y=-132.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-112.3):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Note(default_x=23.09, default_y=-87.3):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=35.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0, relative_x=-20.0)
                Staff(2)
            with Note(default_x=78.56, default_y=-112.3):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=78.56, default_y=-92.3):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=78.56, default_y=-82.3):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=97.01, default_y=-147.3):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=2.12)
                Staff(2)
        with Measure(number='54', width=109.78):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=19.66, relative_y=-41.23):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-30.0):
                Grace(slash='yes')
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Fermata(None, type='upright', default_y=34.13, relative_y=10.0)
            with Note(default_x=13.8, default_y=-5.0):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=32.24, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(7)
                Duration(36.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', default_y=34.13, relative_y=10.0)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=6.14)
                Staff(1)
            with Backup():
                Duration(36.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.18)
                Staff(2)
            with Note(default_x=13.8, default_y=-132.3):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Fermata(None, type='inverted', default_y=-49.45, relative_y=-10.0)
            with Note(default_x=13.8, default_y=-112.3):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-87.3):
                Grace(slash='yes')
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=32.24, default_y=-167.3):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(36.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='inverted', default_y=-49.45, relative_y=-10.0)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')