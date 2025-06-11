with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('12 ÉTUDES')
    with Identification():
        Creator('F. Chopin', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/16916841/scores/6307507')
    with Defaults():
        with Scaling():
            Millimeters(7.05556)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1584.0)
            PageWidth(1224.0)
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
        CreditWords('12 ÉTUDES', default_x=612.0, default_y=1527.31, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Op. 10 No. 3', default_x=612.0, default_y=1470.61, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('F. Chopin', default_x=1167.31, default_y=1427.31, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=174.2):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(213.64)
                with StaffLayout(number=2):
                    StaffDistance(103.58)
            with Attributes():
                Divisions(60.0)
                with Key():
                    Fifths(4)
                with Time():
                    Beats('2')
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
                    Words('Lento, ma non troppo. ', default_x=-39.8, default_y=70.44, relative_y=20.0, font_weight='bold', font_size='12')
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-39.8, default_y=70.44, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-42.8, relative_x=4.93, relative_y=-34.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=56.89, relative_x=2.93, relative_y=6.95):
                        OtherDynamics('legato')
                Staff(1)
            with Note(default_x=134.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(30.0)
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='1', width=240.17):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=70.99)
                Staff(1)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=71.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=99.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=127.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=43.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=71.49, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.18, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=155.03, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=182.88, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.72, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=127.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=43.65, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=99.34, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=127.18, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=155.03, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=210.72, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.18, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=244.59):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=30.08)
                Staff(1)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=44.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.59)
                Staff(1)
            with Note(default_x=72.6, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=129.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=129.4, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.6, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=129.4, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=157.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.19, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=72.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(60.0)
            with Note(default_x=15.8, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=44.2, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=101.0, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=129.4, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=157.79, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=214.59, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=129.4, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='3', width=203.02):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=85.39)
                Staff(1)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=90.99)
                Staff(1)
            with Note(default_x=62.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=85.18, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=101.39)
                Staff(1)
            with Note(default_x=108.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=178.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-50.0)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=62.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=85.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=108.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=132.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=155.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=178.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=38.93, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.18, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=108.31, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=132.0, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.26, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=108.31, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=227.63):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=42.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=68.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=94.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=120.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=42.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=68.36, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=94.64, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=120.91, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=120.91, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-15.0)
                Staff(1)
            with Note(default_x=147.19, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.19, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=173.47, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.47, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=199.75, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.75, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=42.08, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.64, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=120.91, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=147.19, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.75, default_y=-173.58):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-193.58):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=120.91, default_y=-208.58):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=340.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(112.8)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=24.45)
                Staff(1)
            with Note(default_x=113.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=70.59)
                Staff(1)
            with Note(default_x=169.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=197.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=226.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.41, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=141.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.59, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=169.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.77, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=197.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=197.95, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=226.12, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.48, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-217.8):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=141.59, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.95, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=226.12, default_y=-202.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=254.3, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=310.66, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-217.8):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=226.12, default_y=-202.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='6', width=190.86):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-108.45)
                Staff(1)
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=35.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.19, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.39, relative_x=25.44, relative_y=-70.07):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=100.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=122.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=35.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.19, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=100.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=122.64, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-202.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=35.73, default_y=-167.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=79.19, default_y=-167.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=100.91, default_y=-187.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=122.64, default_y=-167.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.1, default_y=-167.8):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-202.8):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=100.91, default_y=-187.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=263.24):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.62, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Note(default_x=170.89, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=189.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        Accent()
            with Note(default_x=214.74, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='start')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.21, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.62, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=92.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction():
                with DirectionType():
                    Words('stretto', default_y=-52.47, relative_y=-50.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=117.44, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.33, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-187.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=41.21, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=92.03, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=117.44, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=142.85, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.74, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-187.8):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=117.44, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=295.08):
            with Note(default_x=21.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.7, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=96.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=124.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', relative_y=57.0, font_style='italic', font_family='Times New Roman', font_size='11.9992')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('riten.', default_y=-59.56, relative_y=-50.0, font_style='italic')
                Staff(1)
            with Note(default_x=178.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=178.96, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=21.03, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=49.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.14, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.63, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.96, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=236.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.85, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=21.03, default_y=-177.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=49.66, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.77, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=178.96, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=207.59, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.85, default_y=-162.8):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=21.03, default_y=-177.8):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=178.96, default_y=-182.8):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=356.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(114.71)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=16.05, relative_y=60.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-80.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=113.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=113.41, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=173.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=204.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=234.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-138.28)
                Staff(1)
            with Note(default_x=143.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=173.89, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=234.37, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=264.61, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=294.85, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.09, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=234.37, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=143.65, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=204.13, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=234.37, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=264.61, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=325.09, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=234.37, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='10', width=263.74):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=30.48)
                Staff(1)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=75.59)
                Staff(1)
            with Note(default_x=77.38, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=108.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=138.97, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=138.97, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.38, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.55, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=77.38, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(60.0)
            with Note(default_x=15.8, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=46.59, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=108.18, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=138.97, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=169.76, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.34, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=138.97, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='11', width=222.17):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=105.39)
                Staff(1)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=102.59)
                Staff(1)
            with Note(default_x=66.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=92.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=101.39)
                Staff(1)
            with Note(default_x=118.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=194.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-50.0)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=66.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=92.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=118.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=143.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=169.38, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=194.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=41.4, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.59, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=118.19, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=143.78, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.97, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=118.19, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=246.78):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=44.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=73.14, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=101.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=130.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=44.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=73.14, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=101.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=130.49, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=130.49, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=159.16, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.16, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=187.83, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.83, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=216.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.5, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=44.47, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.82, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=130.49, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=159.16, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.5, default_y=-184.71):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-204.71):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.49, default_y=-219.71):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=347.48):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(111.69)
                with StaffLayout(number=2):
                    StaffDistance(92.51)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=24.61)
                Staff(1)
            with Note(default_x=113.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=142.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=70.59)
                Staff(1)
            with Note(default_x=171.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=200.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=229.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.41, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=142.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.47, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=171.53, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.53, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=200.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note(default_x=200.59, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=229.65, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=258.7, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.76, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.82, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-197.51):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=142.47, default_y=-162.51):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=200.59, default_y=-162.51):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=229.65, default_y=-182.51):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=258.7, default_y=-162.51):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.82, default_y=-162.51):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-197.51):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=229.65, default_y=-182.51):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='14', width=197.91):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=31.14, relative_y=-53.77):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=36.73, default_y=-15.0, dynamics=60.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=59.47, default_y=-15.0, dynamics=63.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=82.2, default_y=-20.0, dynamics=65.56):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=104.94, default_y=-25.0, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=127.67, default_y=-20.0, dynamics=71.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.41, default_y=-30.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=173.14, default_y=-25.0, dynamics=76.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=14.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=36.73, default_y=-40.0, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=36.73, default_y=-30.0, dynamics=60.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=59.47, default_y=-45.0, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.47, default_y=-35.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=82.2, default_y=-40.0, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=82.2, default_y=-30.0, dynamics=65.56):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=104.94, default_y=-50.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.67, default_y=-40.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.41, default_y=-50.0, dynamics=74.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.14, default_y=-40.0, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-182.51):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=36.73, default_y=-147.51, dynamics=60.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=82.2, default_y=-147.51, dynamics=65.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=104.94, default_y=-167.51, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=127.67, default_y=-147.51, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=173.14, default_y=-147.51, dynamics=76.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-182.51):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=104.94, default_y=-167.51, dynamics=68.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=236.12):
            with Direction():
                with DirectionType():
                    Words('stretto', default_y=-45.13, relative_y=-40.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=29.26, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=53.51, default_y=-5.0, dynamics=82.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.4, default_y=-5.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.65, default_y=-10.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=71.21, relative_y=-57.08):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=131.89, default_y=-15.0, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=156.13, default_y=-10.0, dynamics=93.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.03, default_y=-20.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=210.27, default_y=-15.0, dynamics=98.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=29.26, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=29.26, default_y=-20.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=53.51, default_y=-30.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.4, default_y=-35.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.4, default_y=-25.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=107.65, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.65, default_y=-20.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=131.89, default_y=-40.0, dynamics=91.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.13, default_y=-30.0, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=186.03, default_y=-40.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.27, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=29.26, default_y=-172.51, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
                        Fingering('5')
            with Note(default_x=53.51, default_y=-137.51, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.65, default_y=-137.51, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=131.89, default_y=-157.51, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=156.13, default_y=-137.51, dynamics=93.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.27, default_y=-137.51, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=29.26, default_y=-172.51, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.89, default_y=-157.51, dynamics=91.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=308.11):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=21.0, relative_x=45.39, relative_y=35.4):
                        OtherDynamics('con forza')
                Staff(1)
            with Note(default_x=29.1, default_y=-40.0, dynamics=102.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=29.1, default_y=-25.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=29.1, default_y=-5.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=63.22, default_y=-35.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=63.22, default_y=-25.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=63.22, default_y=0.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('ritenuto', default_y=-53.98, relative_y=-40.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=97.35, default_y=-45.0, dynamics=107.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=97.35, default_y=-25.0, dynamics=107.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=97.35, default_y=-10.0, dynamics=107.78):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=131.47, default_y=-40.0, dynamics=110.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=131.47, default_y=-25.0, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=131.47, default_y=-5.0, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=170.01, default_y=-35.0, dynamics=113.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=170.01, default_y=-25.0, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=170.01, default_y=0.0, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=192.27, default_y=-30.0, dynamics=115.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=204.13, default_y=-25.0, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=204.13, default_y=5.0, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=238.26, default_y=-40.0, dynamics=118.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=238.26, default_y=-25.0, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=238.26, default_y=-5.0, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=272.38, default_y=-35.0, dynamics=121.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=272.38, default_y=-25.0, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=272.38, default_y=0.0, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=29.1, default_y=-157.51, dynamics=102.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=17.23, default_y=-147.51, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=29.1, default_y=-142.51, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=29.1, default_y=-132.51, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=63.22, default_y=-157.51, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.36, default_y=-147.51, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=63.22, default_y=-142.51, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=63.22, default_y=-132.51, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=97.35, default_y=-157.51, dynamics=107.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.48, default_y=-147.51, dynamics=107.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=97.35, default_y=-142.51, dynamics=107.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=97.35, default_y=-132.51, dynamics=107.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.47, default_y=-157.51, dynamics=110.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=119.61, default_y=-147.51, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.47, default_y=-142.51, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.47, default_y=-132.51, dynamics=110.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=170.01, default_y=-157.51, dynamics=113.33):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=158.14, default_y=-147.51, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=170.01, default_y=-142.51, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=170.01, default_y=-132.51, dynamics=113.33):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.13, default_y=-157.51, dynamics=115.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.27, default_y=-147.51, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.13, default_y=-142.51, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.13, default_y=-132.51, dynamics=115.56):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=238.26, default_y=-157.51, dynamics=118.89):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.39, default_y=-147.51, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=238.26, default_y=-142.51, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=238.26, default_y=-132.51, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=272.38, default_y=-157.51, dynamics=121.11):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.52, default_y=-147.51, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=272.38, default_y=-142.51, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=272.38, default_y=-132.51, dynamics=121.11):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=311.4):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(110.65)
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', default_y=12.02, relative_x=-6.0, relative_y=55.0, font_style='italic', font_family='Times New Roman', font_size='11.9992')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-60.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=109.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=109.97, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.3)
                Staff(1)
            with Note(default_x=199.07, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=220.35, default_y=0.0, dynamics=117.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=241.63, default_y=-5.0, dynamics=114.44):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=21.0)
                Staff(1)
            with Note(default_x=262.91, default_y=-15.0, dynamics=110.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=109.97, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=131.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=173.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.35, default_y=-20.0, dynamics=117.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.63, default_y=-30.0, dynamics=114.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.77, default_y=-20.0, dynamics=110.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=109.61, default_y=-180.65):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.61, default_y=-165.65):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.61, default_y=-155.65):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=109.61, default_y=-145.65):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=179.99):
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', relative_x=-6.0, relative_y=55.0, font_style='italic', font_family='Times New Roman', font_size='11.9992')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-57.53, relative_x=72.35, relative_y=-65.86):
                        OtherDynamics('sempre legato')
                Staff(1)
            with Note(default_x=15.23, default_y=-10.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=95.23, default_y=-5.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=115.23, default_y=-10.0, dynamics=88.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=135.23, default_y=-15.0, dynamics=85.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=155.23, default_y=-30.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.23, default_y=-45.0, dynamics=106.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=35.23, default_y=-35.0, dynamics=103.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=55.23, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.23, default_y=-35.0, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.23, default_y=-40.0, dynamics=93.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.23, default_y=-30.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.23, default_y=-40.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.23, default_y=-30.0, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.23, default_y=-160.65, dynamics=106.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=35.23, default_y=-145.65, dynamics=103.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.23, default_y=-180.65, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.23, default_y=-145.65, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=95.23, default_y=-175.65, dynamics=93.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=115.23, default_y=-155.65, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.23, default_y=-190.65, dynamics=85.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.23, default_y=-155.65, dynamics=82.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='19', width=205.64):
            with Direction(placement='above'):
                with DirectionType():
                    Words('ten.', relative_x=4.0, relative_y=65.0, font_style='italic', font_family='Times New Roman', font_size='11.9992')
                Staff(1)
            with Note(default_x=15.8, default_y=-20.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.81, relative_x=3.03, relative_y=-58.74):
                        OtherDynamics('dim.')
                Staff(1)
            with Note(default_x=109.92, default_y=-15.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=133.45, default_y=-20.0, dynamics=61.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=156.98, default_y=-25.0, dynamics=57.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=180.51, default_y=-40.0, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=78.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.33, default_y=-45.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.86, default_y=-55.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.39, default_y=-45.0, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.92, default_y=-50.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.45, default_y=-40.0, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.98, default_y=-50.0, dynamics=57.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.51, default_y=-40.0, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-170.65, dynamics=78.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=39.33, default_y=-155.65, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.86, default_y=-190.65, dynamics=72.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.39, default_y=-155.65, dynamics=67.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.92, default_y=-185.65, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=133.45, default_y=-165.65, dynamics=61.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.98, default_y=-200.65, dynamics=57.78):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.51, default_y=-165.65, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=259.53):
            with Note(default_x=15.44, default_y=-30.0, dynamics=51.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(96.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Note(default_x=198.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=235.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('16th', size='cue')
                with TimeModification():
                    ActualNotes(10)
                    NormalNotes(8)
                    NormalType('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0, dynamics=51.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('rall.', default_y=-61.8, relative_x=20.0, relative_y=-50.0, font_style='italic')
                Staff(1)
            with Note(default_x=41.98, default_y=-55.0, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.16, default_y=-65.0, dynamics=43.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.34, default_y=-55.0, dynamics=40.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.93, relative_x=-0.59, relative_y=-67.1):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=120.52, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.7, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.88, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-180.65, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=41.98, default_y=-165.65, dynamics=46.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.16, default_y=-200.65, dynamics=43.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.34, default_y=-165.65, dynamics=40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=120.52, default_y=-180.65):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.7, default_y=-165.65):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.88, default_y=-200.65):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.2, default_y=-180.65):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Tie(type='start')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(90.0)
            with Note(default_x=172.88, default_y=-200.65):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(30.0)
                Tie(type='start')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='21', width=133.04):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-1.3, relative_y=-53.2):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('poco più animoto', default_y=49.7, relative_y=60.0, font_style='italic')
                Staff(1)
            with Note(default_x=54.92, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('2')
            with Note(default_x=54.92, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=72.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=72.71, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=90.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.49, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=108.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=108.28, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(60.0)
            with Note(default_x=15.8, default_y=-180.65):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(60.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=15.8, default_y=-165.65):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-200.65):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(60.0)
        with Measure(number='22', width=333.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(181.9)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=109.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=109.61, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=139.51, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=166.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.64, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=193.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=193.78, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=220.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=250.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=277.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=220.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=277.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=109.61, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=139.51, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=166.64, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=193.78, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=220.92, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=250.81, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=277.95, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=305.08, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='23', width=253.74):
            with Note(default_x=24.37, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('4')
            with Note(default_x=42.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1')
            with Note(default_x=42.81, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=67.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=67.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=85.01, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=103.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=103.45, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=128.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=128.24, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-1.3, relative_y=-53.2):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=153.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=153.02, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=177.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=202.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.58, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=227.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=227.36, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=42.81, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=67.6, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.45, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='24', width=236.21):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=12.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=41.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=41.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=69.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=96.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=96.17, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=123.3, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=153.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=180.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=123.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=180.34, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.47, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=69.03, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.17, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=123.3, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=153.2, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=180.34, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.47, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='25', width=265.84):
            with Note(default_x=24.37, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('4')
            with Note(default_x=42.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1')
            with Note(default_x=42.81, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=69.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=69.3, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=86.71, default_y=-25.0):
                Grace(slash='yes')
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=105.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=105.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=131.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.64, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-80.68)
                Staff(1)
            with Note(default_x=158.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=158.31, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=184.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.79, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=211.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.28, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=237.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=237.76, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=42.81, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=69.3, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.16, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note():
                Rest()
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='26', width=342.23):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(151.41)
                with StaffLayout(number=2):
                    StaffDistance(98.75)
            with Note(default_x=109.61, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=109.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=139.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.51, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=167.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.77, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=197.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=197.67, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=225.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=255.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=284.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=225.94, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=284.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=312.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=109.61, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=139.51, default_y=-133.75):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=167.77, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=197.67, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=225.94, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=255.83, default_y=-123.75):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=284.1, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.36, default_y=-133.75):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='27', width=232.14):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-59.25)
                Staff(1)
            with Note(default_x=22.11, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('3')
            with Note(default_x=40.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('2')
            with Note(default_x=40.55, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=62.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=62.38, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=79.8, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=98.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=98.24, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=120.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.06, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-84.92)
                Staff(1)
            with Note(default_x=141.89, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=141.89, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=163.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.72, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=185.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.55, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=207.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=207.37, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=40.55, default_y=-163.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=62.38, default_y=-143.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.24, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='28', width=244.62):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=12.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=41.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=41.9, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=70.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.16, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=100.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=100.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=128.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=158.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=186.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=128.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=186.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=214.75, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.9, default_y=-133.75):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=70.16, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=100.06, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.32, default_y=-178.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=158.22, default_y=-123.75):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=186.49, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.75, default_y=-133.75):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='29', width=270.63):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-61.42)
                Staff(1)
            with Note(default_x=22.11, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('3')
            with Note(default_x=40.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('2')
            with Note(default_x=40.55, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=65.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=65.81, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=83.23, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=101.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=101.67, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=126.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.93, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=144.34, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=162.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=162.79, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=193.25, default_y=-40.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.25, default_y=-30.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=-8.44, relative_y=-38.32):
                        OtherDynamics('cresc.')
                Staff(1)
            with Note(default_x=218.51, default_y=-35.0, dynamics=85.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.51, default_y=-25.0, dynamics=85.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=243.77, default_y=-30.0, dynamics=96.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.77, default_y=-20.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=40.55, default_y=-163.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=65.81, default_y=-143.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.67, default_y=-128.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=126.93, default_y=-163.75):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=162.79, default_y=-168.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=193.25, default_y=-123.75, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=218.51, default_y=-153.75, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.77, default_y=-168.75, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4', placement='below')
        with Measure(number='30', width=394.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(104.68)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.49, relative_x=1.69, relative_y=-50.7):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=110.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=110.67, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=216.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=216.42, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=251.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=251.67, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=357.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=357.43, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=145.92, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=145.92, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=181.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=181.17, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=286.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=286.93, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=310.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=322.18, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=145.92, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=181.17, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(45.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=286.93, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=322.18, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=110.67, default_y=-179.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=216.42, default_y=-194.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=251.67, default_y=-174.68):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=357.43, default_y=-194.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='31', width=323.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.59, relative_x=-3.82, relative_y=-46.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=14.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=129.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=129.49, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=167.99, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=167.99, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
                        Fingering('5')
            with Note(default_x=283.47, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=283.47, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=52.5, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.5, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=90.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=90.99, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=206.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=206.48, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=233.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=244.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=52.5, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=90.99, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(45.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=206.48, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=244.98, default_y=-159.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-179.68):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.49, default_y=-194.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=167.99, default_y=-174.68):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=283.47, default_y=-194.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='32', width=371.76):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-57.69, relative_x=1.14, relative_y=-37.22):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=21.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=21.03, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=21.03, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=32.9, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-44.53, relative_x=-3.49, relative_y=-37.01):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-76.54)
                Staff(1)
            with Note(default_x=62.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=62.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=103.61, default_y=-30.0, dynamics=64.44):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=103.61, default_y=-20.0, dynamics=64.44):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=151.84, default_y=-20.0, dynamics=68.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=163.71, default_y=-15.0, dynamics=68.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=205.0, default_y=-5.0, dynamics=73.33):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=205.0, default_y=5.0, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=246.29, default_y=5.0, dynamics=77.78):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=246.29, default_y=15.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=287.58, default_y=-15.0, dynamics=83.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=287.58, default_y=-5.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=328.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=328.87, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-99.7)
                Staff(2)
            with Note(default_x=21.03, default_y=-184.68):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=21.03, default_y=-149.68):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=62.32, default_y=-149.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=62.32, default_y=-139.68):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=103.61, default_y=-134.68, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('2', placement='below')
            with Note(default_x=103.61, default_y=-124.68, dynamics=64.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=163.71, default_y=-184.68, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=163.71, default_y=-174.68, dynamics=68.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=205.0, default_y=-199.68, dynamics=73.33):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=216.86, default_y=-194.68, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=246.29, default_y=-194.68, dynamics=77.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=246.29, default_y=-184.68, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=287.58, default_y=-174.68, dynamics=83.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=287.58, default_y=-164.68, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=317.01, default_y=-164.68):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('2', placement='below')
            with Note(default_x=328.87, default_y=-159.68):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='33', width=459.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(156.74)
                with StaffLayout(number=2):
                    StaffDistance(100.13)
            with Note(default_x=111.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=123.71, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=164.22, default_y=20.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=164.22, default_y=30.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=204.73, default_y=5.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=204.73, default_y=15.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=233.38, default_y=15.0, dynamics=96.67):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=245.24, default_y=20.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=285.76, default_y=30.0, dynamics=118.89):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=285.76, default_y=40.0, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.8, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-78.8)
                Staff(1)
            with Note(default_x=336.74, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=336.74, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=377.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=377.25, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=417.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=417.77, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=123.71, default_y=-180.13):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=123.71, default_y=-170.13):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=164.22, default_y=-170.13, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=164.22, default_y=-160.13, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=204.73, default_y=-155.13, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=204.73, default_y=-145.13, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=245.24, default_y=-145.13, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('1', placement='below')
            with Note(default_x=245.24, default_y=-135.13, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=273.89, default_y=-160.13, dynamics=118.89):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=285.76, default_y=-155.13, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=336.74, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=336.74, default_y=-130.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=336.74, default_y=-120.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=377.25, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=377.25, default_y=-130.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=377.25, default_y=-120.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=417.77, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=417.77, default_y=-130.13):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=417.77, default_y=-120.13):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=303.16):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=5.5, relative_y=-67.98):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
                        Fingering('4')
            with Note(default_x=13.06, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=121.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=121.25, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=157.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=157.31, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=265.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=265.5, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=49.12, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('2', placement='below')
            with Note(default_x=49.12, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=85.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=85.18, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=193.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=193.37, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=217.57, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=229.44, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=13.06, default_y=-135.13):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=49.12, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=85.18, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Tie(type='start')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('1')
            with Note(default_x=121.25, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.37, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=229.44, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(30.0)
            with Note(default_x=85.18, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=121.25, default_y=-185.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=157.31, default_y=-165.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=265.5, default_y=-185.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='35', width=326.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=2.82, relative_y=-57.98):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=14.0, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
                        Fingering('4')
            with Note(default_x=130.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=130.62, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=169.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=169.49, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=286.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=286.1, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Staff(1)
            with Note(default_x=52.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=52.87, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=91.74, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=91.74, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(45.0)
                Voice('2')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=208.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=208.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=235.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=247.23, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=52.87, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=91.74, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(45.0)
                Voice('5')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=208.36, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=247.23, default_y=-150.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-170.13):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=130.62, default_y=-185.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=169.49, default_y=-165.13):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(45.0)
                Voice('6')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=286.1, default_y=-185.13):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='36', width=379.35):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    TopSystemDistance(137.6)
                with StaffLayout(number=2):
                    StaffDistance(113.76)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-52.69, relative_x=1.14, relative_y=-37.22):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=121.65, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=121.65, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=121.65, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=133.52, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.99, relative_x=-3.49, relative_y=-37.01):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=151.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=151.77, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=187.07, default_y=-25.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=187.07, default_y=-15.0, dynamics=64.44):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=215.32, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=227.19, default_y=-10.0, dynamics=68.89):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=257.3, default_y=0.0, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=257.3, default_y=10.0, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=287.41, default_y=10.0, dynamics=77.78):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=287.41, default_y=20.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=317.53, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=317.53, default_y=0.0, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=347.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=347.64, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-94.7)
                Staff(2)
            with Note(default_x=121.65, default_y=-188.76):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=121.65, default_y=-153.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=151.77, default_y=-153.76):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=151.77, default_y=-143.76):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=187.07, default_y=-138.76, dynamics=64.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=187.07, default_y=-128.76, dynamics=64.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=227.19, default_y=-188.76, dynamics=68.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=227.19, default_y=-178.76, dynamics=68.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=257.3, default_y=-203.76, dynamics=73.33):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=269.16, default_y=-198.76, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=287.41, default_y=-198.76, dynamics=77.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=287.41, default_y=-188.76, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=317.53, default_y=-178.76, dynamics=83.33):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=317.53, default_y=-168.76, dynamics=83.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=335.77, default_y=-168.76):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('2', placement='below')
            with Note(default_x=347.64, default_y=-163.76):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='37', width=306.94):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=27.67, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=59.59, default_y=25.0, dynamics=87.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=59.59, default_y=35.0, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=91.52, default_y=10.0, dynamics=92.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.52, default_y=20.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=114.79, default_y=20.0, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=126.65, default_y=25.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-17.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=158.58, default_y=35.0, dynamics=118.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.58, default_y=45.0, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
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
            with Note(default_x=209.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=209.56, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=241.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=241.49, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=273.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=273.42, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=27.67, default_y=-188.76):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=27.67, default_y=-178.76):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=59.59, default_y=-178.76, dynamics=87.78):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=59.59, default_y=-168.76, dynamics=87.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=91.52, default_y=-163.76, dynamics=92.22):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.52, default_y=-153.76, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=126.65, default_y=-153.76, dynamics=96.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('1', placement='below')
            with Note(default_x=126.65, default_y=-143.76, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=146.71, default_y=-168.76, dynamics=118.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=158.58, default_y=-163.76, dynamics=118.89):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=209.56, default_y=-158.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=209.56, default_y=-138.76):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=209.56, default_y=-128.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=241.49, default_y=-158.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=241.49, default_y=-138.76):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=241.49, default_y=-128.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=273.42, default_y=-158.76):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=273.42, default_y=-138.76):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=273.42, default_y=-128.76):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='38', width=403.32):
            with Note(default_x=41.7, default_y=-20.0, dynamics=64.44):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=41.7, default_y=-5.0, dynamics=64.44):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.44, relative_y=-48.02):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=86.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=86.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=131.7, default_y=-30.0, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=131.7, default_y=-15.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=176.7, default_y=-15.0, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=176.7, default_y=0.0, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=221.71, default_y=-20.0, dynamics=72.22):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=221.71, default_y=-5.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=266.71, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=266.71, default_y=10.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-90.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-90.0)
                Staff(1)
            with Note(default_x=311.71, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=311.71, default_y=10.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=356.72, default_y=5.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=356.72, default_y=25.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=41.7, default_y=-158.76, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=29.83, default_y=-138.76, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=41.7, default_y=-133.76, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=86.7, default_y=-163.76):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=86.7, default_y=-148.76):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=51.71)
                Staff(2)
            with Note(default_x=131.7, default_y=-168.76, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=131.7, default_y=-153.76, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=176.7, default_y=-173.76, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=176.7, default_y=-153.76, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=221.71, default_y=-173.76, dynamics=72.22):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=221.71, default_y=-158.76, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=266.71, default_y=-178.76, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=266.71, default_y=-158.76, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=311.71, default_y=-178.76, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=311.71, default_y=-163.76, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=27.0)
                Staff(2)
            with Note(default_x=356.72, default_y=-183.76, dynamics=84.44):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=356.72, default_y=-163.76, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='39', width=606.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(220.25)
                with StaffLayout(number=2):
                    StaffDistance(122.74)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=134.24, default_y=5.0, dynamics=88.89):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1')
            with Note(default_x=134.24, default_y=20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=4.44, relative_y=-48.02):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=193.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=193.04, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=251.83, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=251.83, default_y=-15.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=310.62, default_y=-20.0, dynamics=67.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=310.62, default_y=0.0, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=369.41, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=369.41, default_y=-5.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=428.2, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=428.2, default_y=10.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-90.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-90.0)
                Staff(1)
            with Note(default_x=487.0, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=487.0, default_y=5.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=545.79, default_y=5.0, dynamics=84.44):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=545.79, default_y=20.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=134.24, default_y=-197.74, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=134.24, default_y=-177.74, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=193.04, default_y=-177.74):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    Slur(type='start', placement='above', number=3)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=193.04, default_y=-162.74):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=60.69)
                Staff(2)
            with Note(default_x=251.83, default_y=-182.74, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=251.83, default_y=-162.74, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=310.62, default_y=-182.74, dynamics=67.78):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=310.62, default_y=-167.74, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=369.41, default_y=-187.74, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=369.41, default_y=-167.74, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=428.2, default_y=-187.74, dynamics=75.56):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=428.2, default_y=-172.74, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=487.0, default_y=-192.74, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=487.0, default_y=-172.74, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=27.0)
                Staff(2)
            with Note(default_x=545.79, default_y=-197.74, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=545.79, default_y=-177.74, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='40', width=483.43):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-50.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=29.83, default_y=0.0, dynamics=88.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('1')
            with Note(default_x=29.83, default_y=20.0, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-85.0)
                Staff(1)
            with Note(default_x=86.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=86.33, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=142.83, default_y=-35.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=142.83, default_y=-20.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=199.33, default_y=-25.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=199.33, default_y=-5.0, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=255.83, default_y=-25.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=255.83, default_y=-10.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=312.33, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=312.33, default_y=5.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=368.83, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=368.83, default_y=5.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=425.33, default_y=0.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=425.33, default_y=20.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Note(default_x=29.83, default_y=-197.74, dynamics=88.89):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
                    with Articulations():
                        Staccato()
            with Note(default_x=29.83, default_y=-182.74, dynamics=88.89):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=86.33, default_y=-182.74):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=86.33, default_y=-162.74):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=142.83, default_y=-182.74, dynamics=63.33):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=142.83, default_y=-167.74, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=199.33, default_y=-187.74, dynamics=67.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=199.33, default_y=-167.74, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=255.83, default_y=-187.74, dynamics=72.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=255.83, default_y=-172.74, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=312.33, default_y=-192.74, dynamics=75.56):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=312.33, default_y=-172.74, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=368.83, default_y=-197.74, dynamics=80.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=368.83, default_y=-177.74, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=425.33, default_y=-197.74, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=425.33, default_y=-182.74, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='41', width=504.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(235.09)
                with StaffLayout(number=2):
                    StaffDistance(102.23)
            with Note(default_x=122.21, default_y=0.0, dynamics=63.33):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=122.21, default_y=15.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=169.65, default_y=10.0, dynamics=67.78):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=169.65, default_y=30.0, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=217.1, default_y=10.0, dynamics=72.22):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=217.1, default_y=25.0, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=150.88)
                Staff(1)
            with Note(default_x=264.54, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=264.54, default_y=5.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=311.98, default_y=-15.0, dynamics=80.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=311.98, default_y=5.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=359.42, default_y=0.0, dynamics=84.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=359.42, default_y=20.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=406.87, default_y=-5.0, dynamics=80.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1')
            with Note(default_x=406.87, default_y=15.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=455.25, default_y=10.0, dynamics=84.44):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=455.25, default_y=30.0, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=122.21, default_y=-182.23):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=122.21, default_y=-162.23):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=169.65, default_y=-182.23, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=169.65, default_y=-167.23, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=217.1, default_y=-187.23, dynamics=67.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=217.1, default_y=-167.23, dynamics=67.78):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=264.54, default_y=-187.23, dynamics=72.22):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=264.54, default_y=-172.23, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=311.98, default_y=-192.23, dynamics=72.22):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=311.98, default_y=-177.23, dynamics=72.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=359.42, default_y=-197.23, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=359.42, default_y=-177.23, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=406.87, default_y=-197.23, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
                        Fingering('4', placement='below')
            with Note(default_x=406.87, default_y=-182.23, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=455.25, default_y=-202.23, dynamics=84.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('5', placement='below')
            with Note(default_x=455.25, default_y=-187.23, dynamics=84.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
        with Measure(number='42', width=257.63):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-120.0)
                Staff(1)
            with Note(default_x=21.03, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=21.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('1')
                        Fingering('4')
            with Note(default_x=46.3, default_y=-10.0, dynamics=75.56):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=46.3, default_y=15.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=74.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=74.71, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=13.0)
                Staff(1)
            with Note():
                Rest()
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=162.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=162.68, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=193.62, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=193.62, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=21.03, default_y=-207.23):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=21.03, default_y=-187.23):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=110.75, default_y=-152.23):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=110.75, default_y=-127.23):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=137.41, default_y=-167.23):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=137.41, default_y=-142.23):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=230.76, default_y=-162.23):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=230.76, default_y=-137.23):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=327.69):
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-105.0)
                Staff(1)
            with Note(default_x=51.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.73, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=63.59, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=51.73, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=90.4, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.4, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=102.27, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=90.4, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=132.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.73, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=144.6, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=132.73, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-30.0)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.64, relative_x=42.47, relative_y=-64.36):
                        OtherDynamics('con forza')
                Staff(1)
            with Note(default_x=171.4, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.4, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=183.27, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=171.4, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=210.08, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.08, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=221.94, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=210.08, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=248.75, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.75, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=260.62, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=248.75, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=287.42, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=287.42, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=299.29, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=287.42, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=13.06, default_y=-177.23):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.06, default_y=-152.23):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=51.73, default_y=-202.23):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.73, default_y=-167.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=90.4, default_y=-207.23):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.4, default_y=-172.23):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=132.73, default_y=-212.23):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.73, default_y=-177.23):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=171.4, default_y=-207.23):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=171.4, default_y=-172.23):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=210.08, default_y=-202.23):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=210.08, default_y=-167.23):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=248.75, default_y=-207.23):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.75, default_y=-172.23):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=287.42, default_y=-212.23):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=287.42, default_y=-177.23):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='44', width=356.98):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(149.42)
                with StaffLayout(number=2):
                    StaffDistance(89.97)
            with Note(default_x=113.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=113.41, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=113.41, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=113.41, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=141.42)
                Staff(1)
            with Note(default_x=141.21, default_y=10.0, dynamics=75.56):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('5')
                        Fingering('2')
            with Note(default_x=141.21, default_y=25.0, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=168.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1')
            with Note(default_x=168.95, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1, relative_x=21.0)
                Staff(1)
            with Note():
                Rest()
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=262.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=262.17, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=289.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=289.9, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-194.97):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=113.41, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=206.69, default_y=-129.97, dynamics=75.56):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('5', placement='below')
                        Fingering('2', placement='below')
            with Note(default_x=206.69, default_y=-104.97, dynamics=75.56):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=234.43, default_y=-149.97):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=234.43, default_y=-119.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=327.64, default_y=-139.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=327.64, default_y=-114.97):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=339.9):
            with Note():
                Rest()
                Duration(15.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=42.47, relative_y=-54.36):
                        OtherDynamics('con forza')
                Staff(1)
            with Note(default_x=53.47, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.47, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=65.34, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=53.47, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=93.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.89, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=105.76, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=93.89, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=136.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.22, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=148.09, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=136.22, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=176.64, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.64, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=188.5, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=176.64, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=217.05, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.05, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=228.92, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=217.05, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=257.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.47, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=269.34, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=257.47, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=297.89, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=297.89, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=297.89, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=309.75, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=13.06, default_y=-159.97):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.06, default_y=-129.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=53.47, default_y=-189.97):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.47, default_y=-154.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=93.89, default_y=-194.97):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.89, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=136.22, default_y=-199.97):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=136.22, default_y=-164.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=176.64, default_y=-194.97):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.64, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=217.05, default_y=-189.97):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.05, default_y=-154.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=257.47, default_y=-194.97):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.47, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=297.89, default_y=-199.97):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=297.89, default_y=-164.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='46', width=392.73):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=15.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=15.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=53.29, relative_y=-52.0):
                        OtherDynamics('con bravura')
                Staff(1)
            with Note(default_x=82.66, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2')
            with Note(default_x=82.66, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=126.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=126.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=169.7, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('1')
            with Note(default_x=169.7, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=213.23, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=213.23, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=256.75, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('2')
            with Note(default_x=256.75, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=304.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Technical():
                        Fingering('1')
            with Note(default_x=304.09, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=347.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('1')
            with Note(default_x=347.61, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-194.97):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=15.8, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-117.5)
                Staff(2)
            with Note(default_x=82.66, default_y=-174.97):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=82.66, default_y=-149.97):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=126.18, default_y=-159.97):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=126.18, default_y=-129.97):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=169.7, default_y=-164.97):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=169.7, default_y=-139.97):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=213.23, default_y=-184.97):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=213.23, default_y=-159.97):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.1)
                Staff(2)
            with Note(default_x=256.75, default_y=-179.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    Slur(type='start', placement='below', number=4)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=256.75, default_y=-154.97):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=304.09, default_y=-164.97):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=304.09, default_y=-139.97):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=347.61, default_y=-174.97):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    Slur(type='start', placement='below', number=4)
                    with Technical():
                        Fingering('1', placement='below')
                        Fingering('3', placement='below')
            with Note(default_x=347.61, default_y=-144.97):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='47', width=424.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=111.84, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=111.84, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=150.71, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=150.71, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=189.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=189.57, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=228.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=228.44, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=267.3, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=267.3, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=306.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=306.17, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=345.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=345.03, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=383.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=383.9, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=111.84, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
            with Note(default_x=111.84, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=150.71, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=150.71, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=189.57, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=189.57, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=228.44, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=228.44, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=267.3, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=267.3, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=306.17, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=306.17, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=345.03, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
            with Note(default_x=345.03, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=383.9, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=3)
                    Slur(type='start', placement='below', number=4)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=383.9, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='48', width=323.9):
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=17.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=55.86, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=55.86, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=93.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=93.92, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=131.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.99, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=170.05, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=170.05, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=208.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=208.11, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=246.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=246.17, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=284.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=284.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=17.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
            with Note(default_x=17.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=55.86, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=55.86, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=93.92, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note(default_x=93.92, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=131.99, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=131.99, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=170.05, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=170.05, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=208.11, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=208.11, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=246.17, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=246.17, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=284.24, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=284.24, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='49', width=341.35):
            with Note(default_x=17.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=17.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=57.49, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=57.49, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=97.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=97.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=136.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=136.88, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=176.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=176.57, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=220.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=220.67, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=260.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=260.36, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=300.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
                    Slur(type='start', placement='above', number=4)
            with Note(default_x=300.06, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=17.8, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=17.8, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=57.49, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=57.49, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=97.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=97.19, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=136.88, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=5)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=136.88, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=176.57, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=5)
            with Note(default_x=176.57, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=220.67, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=5)
            with Note(default_x=220.67, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=260.36, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=5)
            with Note(default_x=260.36, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=300.06, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=5)
                    Slur(type='start', placement='below', number=6)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=300.06, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='50', width=415.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(70.61)
            with Note(default_x=126.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
            with Note(default_x=126.08, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=161.99, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
                    Slur(type='start', placement='above', number=4)
            with Note(default_x=161.99, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=198.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
                    Slur(type='stop', number=4)
            with Note(default_x=198.49, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=234.4, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=234.4, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=270.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=270.32, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=306.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=306.23, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=342.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=342.14, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=378.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=378.06, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=126.08, default_y=-175.61):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=5)
                    Slur(type='stop', number=6)
            with Note(default_x=126.08, default_y=-145.61):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=161.99, default_y=-165.61):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=4)
                    Slur(type='start', placement='below', number=5)
            with Note(default_x=161.99, default_y=-140.61):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=198.49, default_y=-145.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=4)
                    Slur(type='stop', number=5)
            with Note(default_x=198.49, default_y=-120.61):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=234.4, default_y=-155.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=4)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=234.4, default_y=-130.61):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=270.32, default_y=-175.61):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=4)
            with Note(default_x=270.32, default_y=-145.61):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=306.23, default_y=-170.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=4)
            with Note(default_x=306.23, default_y=-145.61):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=342.14, default_y=-155.61):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=4)
            with Note(default_x=342.14, default_y=-125.61):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=378.06, default_y=-160.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=4)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=378.06, default_y=-135.61):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
        with Measure(number='51', width=320.46):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=15.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-82.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-82.0)
                Staff(1)
            with Note(default_x=52.56, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=52.56, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=89.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=3)
            with Note(default_x=89.32, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=33.29, relative_y=-42.0):
                        OtherDynamics('e stretto')
                Staff(1)
            with Note(default_x=126.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.08, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=162.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=162.84, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=199.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=199.61, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=245.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=245.33, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=282.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=282.1, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-180.61):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=4)
            with Note(default_x=15.8, default_y=-155.61):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=52.56, default_y=-170.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    Slur(type='start', placement='below', number=3)
            with Note(default_x=52.56, default_y=-145.61):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=89.32, default_y=-155.61):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=3)
            with Note(default_x=89.32, default_y=-125.61):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=126.08, default_y=-155.61):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=126.08, default_y=-130.61):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=162.84, default_y=-175.61):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=162.84, default_y=-145.61):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=199.61, default_y=-175.61):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=199.61, default_y=-150.61):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=245.33, default_y=-160.61):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=245.33, default_y=-135.61):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=282.1, default_y=-160.61):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=282.1, default_y=-135.61):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='52', width=353.59):
            with Note(default_x=33.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=33.06, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=69.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.56, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=105.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=105.13, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=174.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.15, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=209.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=209.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=245.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=245.29, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=280.85, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.85, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=316.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=316.42, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=33.06, default_y=-180.61):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=33.06, default_y=-155.61):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=69.56, default_y=-180.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=69.56, default_y=-155.61):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=105.13, default_y=-165.61):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=105.13, default_y=-140.61):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
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
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=174.15, default_y=-110.61):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=174.15, default_y=-80.61):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=209.72, default_y=-125.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=209.72, default_y=-100.61):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=245.29, default_y=-110.61):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=245.29, default_y=-80.61):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=280.85, default_y=-125.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=280.85, default_y=-100.61):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=316.42, default_y=-110.61):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=316.42, default_y=-80.61):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='53', width=389.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(188.27)
                with StaffLayout(number=2):
                    StaffDistance(91.02)
            with Note(default_x=122.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.21, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('ritenuto', default_y=-61.07, relative_y=-20.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=169.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.55, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=201.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=201.62, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=232.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=232.49, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=263.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=263.36, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note(default_x=295.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=295.43, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=326.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=326.3, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=357.17, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=357.17, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=122.21, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=122.21, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=169.55, default_y=-131.02):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=169.55, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=201.62, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=201.62, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=232.49, default_y=-131.02):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=232.49, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=263.36, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=263.36, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.0)
                Staff(2)
            with Note(default_x=295.43, default_y=-131.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=295.43, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=326.3, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=326.3, default_y=-121.02):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-109.13)
                Staff(2)
            with Note(default_x=357.17, default_y=-131.02):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=357.17, default_y=-106.02):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='54', width=196.79):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=15.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-70.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=61.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=83.4, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legatissimo', default_y=-63.18, relative_y=-50.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=105.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=149.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3 4')
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(30.0)
            with Note(default_x=61.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=105.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.87, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=15.8, default_y=-126.02):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note():
                Rest()
                Duration(15.0)
                Voice('5')
                Type('16th')
                Staff(2)
            with Note(default_x=61.25, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=105.56, default_y=-166.02):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=149.87, default_y=-156.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='55', width=251.22):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Words('tempo', default_y=12.29, relative_x=-190.0, relative_y=70.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=73.97, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
                    with Technical():
                        Fingering('5')
            with Note(default_x=110.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=198.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=2)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3 4')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=47.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=73.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=110.62, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.27, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=172.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.45, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=224.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.97, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=94.96, default_y=-141.02):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=126.29, default_y=-146.02):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=147.27, default_y=-166.02):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=198.45, default_y=-156.02):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='below', number=2)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='56', width=251.96):
            with Direction(placement='below'):
                with DirectionType():
                    Words('sempre', default_y=-57.78, relative_x=20.0, relative_y=-50.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=75.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=3)
            with Note(default_x=104.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-70.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=132.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=161.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=193.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=3)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=132.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.36, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=75.8, default_y=-196.02):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=132.8, default_y=-181.02):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=193.36, default_y=-161.02):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='57', width=409.45):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(79.77)
                with StaffLayout(number=2):
                    StaffDistance(87.59)
            with Note(default_x=113.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=147.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=181.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=226.65, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=271.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=305.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=339.89, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('3')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.37, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.65, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=271.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=305.91, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=339.89, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=373.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=181.37, default_y=-192.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=209.24, default_y=-187.59):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=244.07, default_y=-192.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=271.93, default_y=-177.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=339.89, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('1', placement='below')
        with Measure(number='58', width=338.72):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=51.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Note(default_x=135.11, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-121.79)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-121.79)
                Staff(1)
            with Note(default_x=182.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=218.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=290.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.6, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.4, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=146.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.82, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=218.62, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=302.09, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(90.0)
            with Note(default_x=254.42, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=87.4, default_y=-177.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=116.76, default_y=-172.59):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=153.46, default_y=-177.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=182.82, default_y=-192.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=254.42, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='59', width=341.44):
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=136.3, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=220.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=292.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=51.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=88.11, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=148.16, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.48, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=220.63, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=304.81, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Forward():
                Duration(60.0)
            with Note(default_x=256.79, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=88.11, default_y=-177.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=117.76, default_y=-172.59):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=154.83, default_y=-177.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=184.48, default_y=-157.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
        with Measure(number='60', width=374.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(81.59)
            with Note(default_x=113.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=143.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.05, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Note(default_x=172.68, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.68, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('smorzando e rallent.', default_y=3.93, relative_x=20.0, relative_y=27.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=202.32, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=202.32, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=231.95, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=231.95, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=261.59, default_y=-50.0, dynamics=51.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.46, default_y=-45.0, dynamics=51.11):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=292.92, default_y=-70.0, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=292.92, default_y=-40.0, dynamics=50.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=332.89, default_y=-50.0, dynamics=48.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=344.76, default_y=-45.0, dynamics=48.89):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(30.0)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=292.92, default_y=-166.59, dynamics=50.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='below', number=2)
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=317.22, default_y=-161.59, dynamics=48.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=348.56, default_y=-166.59, dynamics=47.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(10.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
                    with Technical():
                        Fingering('2', placement='below')
        with Measure(number='61', width=236.91):
            with Note(default_x=15.8, default_y=-70.0, dynamics=46.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=15.8, default_y=-40.0, dynamics=46.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=43.24, default_y=-60.0, dynamics=45.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=43.24, default_y=-45.0, dynamics=45.56):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=70.68, default_y=-70.0, dynamics=44.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.68, default_y=-40.0, dynamics=44.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=98.12, default_y=-60.0, dynamics=42.22):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.12, default_y=-45.0, dynamics=42.22):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=125.56, default_y=-70.0, dynamics=41.11):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=125.56, default_y=-40.0, dynamics=41.11):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=152.99, default_y=-55.0, dynamics=40.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.99, default_y=-45.0, dynamics=40.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=180.43, default_y=-70.0, dynamics=37.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.43, default_y=-50.0, dynamics=37.78):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=207.87, default_y=-55.0, dynamics=36.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.87, default_y=-45.0, dynamics=36.67):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-186.59, dynamics=46.67):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note():
                Rest()
                Duration(60.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='62', width=236.91):
            with Direction():
                with DirectionType():
                    Words('tempo I', default_y=46.49, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=6.58, relative_y=-70.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=70.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=98.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=125.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5 4')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=152.99, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Forward():
                Duration(60.0)
            with Note(default_x=125.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-171.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=43.24, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.12, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=125.56, default_y=-186.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=152.99, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.87, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-171.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=125.56, default_y=-186.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='63', width=241.33):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=43.79, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=71.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=127.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=127.77, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.78, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.77, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=127.77, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=183.75, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=211.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=71.78, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(30.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(60.0)
            with Note(default_x=15.8, default_y=-186.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=43.79, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.77, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=127.77, default_y=-171.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=155.76, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.74, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-186.59):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=127.77, default_y=-171.59):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='64', width=333.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(93.69)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-104.65)
                Staff(1)
            with Note(default_x=113.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=140.77, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=168.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=195.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-93.0)
                Staff(1)
            with Note(default_x=222.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(45.0)
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
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=304.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.77, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=168.13, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=195.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=222.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=250.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=277.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=304.92, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=140.77, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.49, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=222.85, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=250.2, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=304.92, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=222.85, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='65', width=260.87):
            with Note(default_x=15.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=46.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=76.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Note(default_x=107.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('3')
            with Note(default_x=137.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=46.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=76.67, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=107.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=137.54, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=137.54, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=167.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.97, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=198.4, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.4, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=228.84, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=228.84, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=46.23, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=107.1, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=137.54, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=167.97, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=228.84, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=137.54, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='66', width=273.41):
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=43.02)
                Staff(1)
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=95.59)
                Staff(1)
            with Note(default_x=79.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=143.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=15.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=47.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=47.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=79.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=111.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=111.8, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=143.81, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.81, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.81, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.81, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=47.8, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.8, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=143.81, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
            with Note(default_x=175.81, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.81, default_y=-163.69):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-198.69):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=143.81, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
        with Measure(number='67', width=221.45):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=39.73, default_y=-15.0, dynamics=58.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=65.46, default_y=-15.0, dynamics=61.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=91.19, default_y=-20.0, dynamics=63.33):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.93, default_y=-25.0, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=142.66, default_y=-20.0, dynamics=66.67):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.39, default_y=-30.0, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=194.12, default_y=-25.0, dynamics=71.11):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=14.0, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=39.73, default_y=-40.0, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=39.73, default_y=-30.0, dynamics=58.89):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=65.46, default_y=-45.0, dynamics=61.11):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.46, default_y=-35.0, dynamics=61.11):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=91.19, default_y=-40.0, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.19, default_y=-30.0, dynamics=63.33):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=116.93, default_y=-50.0, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=142.66, default_y=-40.0, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.39, default_y=-50.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.12, default_y=-40.0, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=24.05, relative_y=36.77):
                        OtherDynamics('poco cresc.')
                Staff(2)
            with Note(default_x=39.73, default_y=-148.69, dynamics=58.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.19, default_y=-148.69, dynamics=63.33):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=116.93, default_y=-168.69, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=142.66, default_y=-148.69, dynamics=66.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.12, default_y=-148.69, dynamics=71.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=14.0, default_y=-183.69):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=116.93, default_y=-168.69, dynamics=64.44):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='68', width=347.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(92.95)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-100.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-100.0)
                Staff(1)
            with Note(default_x=133.68, default_y=-10.0, dynamics=73.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=159.04, default_y=-5.0, dynamics=75.56):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.93, default_y=-5.0, dynamics=77.78):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=14.05, relative_y=-60.23):
                        OtherDynamics('e.')
                Staff(1)
            with Note(default_x=214.29, default_y=-10.0, dynamics=80.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=34.05, relative_y=-60.23):
                        OtherDynamics('stretto')
                Staff(1)
            with Note(default_x=239.64, default_y=-15.0, dynamics=81.11):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=264.99, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.89, default_y=-20.0, dynamics=85.56):
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=320.24, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=133.68, default_y=-35.0, dynamics=73.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.68, default_y=-20.0, dynamics=73.33):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=159.04, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.93, default_y=-35.0, dynamics=77.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.93, default_y=-25.0, dynamics=77.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=214.29, default_y=-30.0, dynamics=80.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=214.29, default_y=-20.0, dynamics=80.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=239.64, default_y=-40.0, dynamics=81.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.99, default_y=-30.0, dynamics=83.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.89, default_y=-40.0, dynamics=85.56):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.24, default_y=-30.0, dynamics=87.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=133.68, default_y=-172.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=159.04, default_y=-137.95, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.29, default_y=-137.95, dynamics=63.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=239.64, default_y=-157.95, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=264.99, default_y=-137.95, dynamics=66.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(30.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=320.24, default_y=-137.95, dynamics=71.11):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=133.68, default_y=-172.95):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.64, default_y=-157.95, dynamics=64.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(60.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='69', width=314.76):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-115.23)
                Staff(1)
            with Note(default_x=29.1, default_y=-40.0, dynamics=90.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=29.1, default_y=-25.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=29.1, default_y=-5.0, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=64.17, default_y=-35.0, dynamics=92.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=64.17, default_y=-25.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=64.17, default_y=0.0, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=99.25, default_y=-45.0, dynamics=94.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=99.25, default_y=-25.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=99.25, default_y=-10.0, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=134.32, default_y=-40.0, dynamics=96.67):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.32, default_y=-25.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=134.32, default_y=-5.0, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=34.05, relative_y=-80.23):
                        OtherDynamics('ritenuto')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-120.23)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-120.23)
                Staff(1)
            with Note(default_x=172.86, default_y=-35.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.86, default_y=-25.0, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=172.86, default_y=0.0, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=196.07, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=207.93, default_y=-25.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=207.93, default_y=5.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=243.01, default_y=-40.0, dynamics=102.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=243.01, default_y=-25.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=243.01, default_y=-5.0, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=278.08, default_y=-35.0, dynamics=104.44):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=278.08, default_y=-25.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=278.08, default_y=0.0, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=29.1, default_y=-157.95, dynamics=90.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('4', placement='below')
            with Note(default_x=17.23, default_y=-147.95, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=29.1, default_y=-142.95, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=29.1, default_y=-132.95, dynamics=90.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=64.17, default_y=-157.95, dynamics=92.22):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.31, default_y=-147.95, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=64.17, default_y=-142.95, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=64.17, default_y=-132.95, dynamics=92.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=99.25, default_y=-157.95, dynamics=94.44):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.38, default_y=-147.95, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=99.25, default_y=-142.95, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=99.25, default_y=-132.95, dynamics=94.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=134.32, default_y=-157.95, dynamics=96.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.46, default_y=-147.95, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=134.32, default_y=-142.95, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=134.32, default_y=-132.95, dynamics=96.67):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=172.86, default_y=-157.95, dynamics=97.78):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('5', placement='below')
            with Note(default_x=160.99, default_y=-147.95, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=172.86, default_y=-142.95, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=172.86, default_y=-132.95, dynamics=97.78):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=207.93, default_y=-157.95, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.07, default_y=-147.95, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=207.93, default_y=-142.95, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=207.93, default_y=-132.95, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=243.01, default_y=-157.95, dynamics=102.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.14, default_y=-147.95, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=243.01, default_y=-142.95, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=243.01, default_y=-132.95, dynamics=102.22):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=278.08, default_y=-157.95, dynamics=104.44):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=266.22, default_y=-147.95, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=278.08, default_y=-142.95, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=278.08, default_y=-132.95, dynamics=104.44):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
        with Measure(number='70', width=233.47):
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=17.85, relative_x=34.05, relative_y=49.77):
                        OtherDynamics('a tempo')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-49.52, relative_x=6.58, relative_y=-60.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=14.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=14.6, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-82.02)
                Staff(1)
            with Note(default_x=112.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=136.6, default_y=0.0, dynamics=97.78):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=160.79, default_y=-5.0, dynamics=92.22):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note(default_x=184.97, default_y=-15.0, dynamics=87.78):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=14.6, default_y=-30.0, dynamics=98.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=38.78, default_y=-20.0, dynamics=101.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=62.97, default_y=-30.0, dynamics=104.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=87.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=112.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.6, default_y=-20.0, dynamics=97.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.79, default_y=-30.0, dynamics=92.22):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.84, default_y=-20.0, dynamics=87.78):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Backup():
                Duration(120.0)
            with Note(default_x=14.24, default_y=-162.95):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=14.24, default_y=-147.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=14.24, default_y=-137.95):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=14.24, default_y=-127.95):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='71', width=194.2):
            with Note(default_x=12.0, default_y=-10.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Direction(placement='below'):
                with DirectionType():
                    Words('dim.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-100.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-100.0)
                Staff(1)
            with Note(default_x=101.96, default_y=-5.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=124.45, default_y=-10.0, dynamics=74.44):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=146.94, default_y=-15.0, dynamics=68.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=169.43, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=83.33):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('1', placement='below')
            with Note(default_x=34.49, default_y=-35.0, dynamics=82.22):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.98, default_y=-45.0, dynamics=81.11):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.47, default_y=-35.0, dynamics=80.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.96, default_y=-40.0, dynamics=78.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=124.45, default_y=-30.0, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.94, default_y=-40.0, dynamics=68.89):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.43, default_y=-30.0, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=12.0, default_y=-142.95, dynamics=83.33):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=34.49, default_y=-127.95, dynamics=82.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.98, default_y=-162.95, dynamics=81.11):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.47, default_y=-127.95, dynamics=80.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.96, default_y=-157.95, dynamics=78.89):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=124.45, default_y=-137.95, dynamics=74.44):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.94, default_y=-172.95, dynamics=68.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.43, default_y=-137.95, dynamics=75.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='72', width=313.82):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(97.09)
                with StaffLayout(number=2):
                    StaffDistance(105.61)
            with Note(default_x=113.41, default_y=-20.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
                    with Technical():
                        Fingering('5')
            with Note(default_x=212.82, default_y=-15.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=237.67, default_y=-20.0, dynamics=51.11):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('5')
            with Note(default_x=262.52, default_y=-25.0, dynamics=45.56):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Note(default_x=287.37, default_y=-40.0, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-55.0, dynamics=60.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=138.26, default_y=-45.0, dynamics=58.89):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.12, default_y=-55.0, dynamics=57.78):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.97, default_y=-45.0, dynamics=56.67):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.82, default_y=-50.0, dynamics=55.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.67, default_y=-40.0, dynamics=51.11):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.52, default_y=-50.0, dynamics=45.56):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.37, default_y=-40.0, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-165.61, dynamics=60.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=138.26, default_y=-150.61, dynamics=58.89):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.12, default_y=-185.61, dynamics=57.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.97, default_y=-150.61, dynamics=56.67):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.82, default_y=-180.61, dynamics=55.56):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=237.67, default_y=-160.61, dynamics=51.11):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.52, default_y=-195.61, dynamics=45.56):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.37, default_y=-160.61, dynamics=54.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='73', width=263.07):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.69, relative_x=4.5, relative_y=-62.84):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=137.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        Fingering('4')
            with Note(default_x=200.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('3')
            with Note(default_x=230.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=76.83, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.44, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-175.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=46.31, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.83, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.34, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.86, default_y=-170.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=169.93, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.44, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='74', width=263.07):
            with Note(default_x=15.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
                    with Technical():
                        Fingering('5')
            with Note(default_x=137.86, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=200.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.83, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.44, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-175.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=46.31, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.83, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.34, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=137.86, default_y=-170.61):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=169.93, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=200.44, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=230.96, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='75', width=249.65):
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(120.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=44.83, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.86, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.89, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=44.05, relative_y=-82.23):
                        OtherDynamics('rallent.')
                Staff(1)
            with Note(default_x=131.93, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.99, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.02, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-175.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('3', placement='below')
            with Note(default_x=44.83, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.86, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.89, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=131.93, default_y=-175.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Technical():
                        Fingering('2', placement='below')
            with Note(default_x=160.96, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.99, default_y=-195.61):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.02, default_y=-160.61):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='76', width=679.54):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(106.61)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=44.05, relative_y=-82.23):
                        OtherDynamics('smorz.')
                Staff(1)
            with Note(default_x=113.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(60.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=395.67, default_y=-30.0, dynamics=30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=466.24, default_y=-35.0, dynamics=28.89):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('4')
            with Note(default_x=536.8, default_y=-40.0, dynamics=27.78):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('5')
            with Note(default_x=607.37, default_y=-55.0, dynamics=26.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccato()
                    with Technical():
                        Fingering('2')
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.98, default_y=-55.0, dynamics=34.44):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.54, default_y=-65.0, dynamics=33.33):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.11, default_y=-55.0, dynamics=32.22):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=395.67, default_y=-65.0, dynamics=30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=466.24, default_y=-55.0, dynamics=28.89):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=536.8, default_y=-65.0, dynamics=27.78):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=607.37, default_y=-55.0, dynamics=26.67):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(15.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(120.0)
            with Note(default_x=113.41, default_y=-176.61):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.98, default_y=-161.61, dynamics=34.44):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.54, default_y=-196.61, dynamics=33.33):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=325.11, default_y=-161.61, dynamics=32.22):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=395.67, default_y=-176.61, dynamics=30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=466.24, default_y=-161.61, dynamics=28.89):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=536.8, default_y=-196.61, dynamics=27.78):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(15.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=607.37, default_y=-176.61, dynamics=26.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(15.0)
                Tie(type='start')
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tied(type='start')
        with Measure(number='77', width=410.08):
            with Note(default_x=15.8, default_y=-65.0, dynamics=25.56):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(120.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Fermata(None, type='upright', default_y=38.2, relative_y=10.0)
            with Note(default_x=15.8, default_y=-40.0, dynamics=25.56):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(120.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Technical():
                        Fingering('4')
            with Backup():
                Duration(120.0)
            with Note(default_x=15.8, default_y=-196.61, dynamics=25.56):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(120.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-49.45, relative_y=-10.0)
            with Note(default_x=15.8, default_y=-176.61, dynamics=25.56):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(120.0)
                Tie(type='stop')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Barline(location='right'):
                BarStyle('light-heavy')