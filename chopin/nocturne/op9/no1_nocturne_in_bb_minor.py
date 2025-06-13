with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Nocturne')
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
        CreditWords('Nocturne', default_x=841.641, default_y=2324.95, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Op. 9 No. 1 in B♭ minor', default_x=841.641, default_y=2268.26, justify='center', valign='top', font_size='14')
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
        with Measure(number='0', implicit='yes', width=362.27):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(182.6)
                with StaffLayout(number=2):
                    StaffDistance(78.71)
            with Attributes():
                Divisions(480.0)
                with Key():
                    Fifths(-5)
                with Time():
                    Beats('6')
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
                    with Dynamics(default_y=-40.0, relative_y=-40.0):
                        P()
                        OtherDynamics(' espress.')
                Staff(1)
                Sound(dynamics=66.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Larghetto', default_x=-36.0, default_y=0.64, relative_y=50.0, font_weight='bold', font_size='13')
                Staff(1)
                Sound(tempo=116.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='yes', default_x=-36.0, default_y=13.4, relative_x=120.0, relative_y=40.0):
                        BeatUnit('quarter')
                        PerMinute('116')
                Staff(1)
                Sound(tempo=116.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, default_y=56.04, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=141.43, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=177.97, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=214.51, default_y=25.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=70.4, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Staff(1)
                Sound(tempo=92.0)
            with Note(default_x=251.05, default_y=10.0):
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
            with Note(default_x=287.59, default_y=15.0):
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
            with Note(default_x=324.13, default_y=5.0):
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
            with Backup():
                Duration(1440.0)
            with Note():
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='1', width=471.37):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=30.02, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('98')
                Staff(1)
                Sound(tempo=98.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-57.66)
                Staff(1)
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=86.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=8.49, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=163.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=239.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.27, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('110')
                Staff(1)
                Sound(tempo=110.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-57.68, relative_x=-1.33)
                Staff(1)
            with Note(default_x=316.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=354.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=393.14, default_y=-5.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=29.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=431.46, default_y=-15.0):
                with Pitch():
                    Step('C')
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
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-148.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.31, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.63, default_y=-103.71):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.94, default_y=-113.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.26, default_y=-93.71):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.57, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=239.89, default_y=-148.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=278.2, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.51, default_y=-98.71):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.83, default_y=-118.71):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=393.14, default_y=-93.71):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=431.46, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='2', width=715.27):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=0.97, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('116')
                Staff(1)
                Sound(tempo=116.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-61.66)
                Staff(1)
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
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
            with Note(default_x=258.5, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=292.74, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=340.51, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=374.75, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=425.76, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=460.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=512.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=546.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=597.41, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=631.66, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=679.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=10.72, default_y=-148.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.02, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.31, default_y=-103.71):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.61, default_y=-113.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.91, default_y=-93.71):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.2, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
            with Note(default_x=258.5, default_y=-148.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=324.84, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.23, default_y=-103.71):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=486.08, default_y=-113.71):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=567.94, default_y=-93.71):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=647.32, default_y=-128.71):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=829.88):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(116.1)
                with StaffLayout(number=2):
                    StaffDistance(78.61)
            with Note(default_x=120.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=145.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=248.7, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=280.77, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=319.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=347.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=385.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=411.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=450.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=479.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=506.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=545.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=571.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=609.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=634.53, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=673.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=698.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=736.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=763.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=802.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(22)
                    NormalNotes(12)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=120.38, default_y=-148.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.68, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.7, default_y=-103.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.15, default_y=-113.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=363.8, default_y=-93.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=426.81, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=479.54, default_y=-148.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=530.06, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=593.08, default_y=-98.61):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=653.91, default_y=-118.61):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=714.74, default_y=-93.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=778.97, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='4', width=358.91):
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=126.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-58.99)
                Staff(1)
            with Note(default_x=184.01, default_y=15.0):
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
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=241.78, default_y=15.0):
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
                        Staccato()
            with Note(default_x=299.54, default_y=15.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=10.72, default_y=-148.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=39.6, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.49, default_y=-103.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.37, default_y=-113.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.25, default_y=-93.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=155.13, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.01, default_y=-148.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=212.9, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.78, default_y=-103.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=270.66, default_y=-113.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.54, default_y=-93.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.42, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='5', width=360.12):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=1.12, relative_y=-23.99):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=185.98, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=301.13, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=329.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=1.33)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1440.0)
            with Note(default_x=186.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-68.2, relative_x=1.33)
                Staff(1)
            with Note(default_x=243.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=272.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=301.13, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=329.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=14.16, default_y=-173.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_y=55.0):
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Note(default_x=42.86, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.55, default_y=-103.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=100.25, default_y=-118.61):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.95, default_y=-93.61):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=157.65, default_y=-128.61):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=186.34, default_y=-158.61):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=215.04, default_y=-138.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.74, default_y=-113.61):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.43, default_y=-123.61):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.13, default_y=-103.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.83, default_y=-138.61):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='6', width=480.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(142.0)
                with StaffLayout(number=2):
                    StaffDistance(76.85)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=123.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=293.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-53.66)
                Staff(1)
            with Note(default_x=357.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=386.05, default_y=-5.0):
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
            with Note(default_x=414.24, default_y=-10.0):
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
            with Note(default_x=450.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-4.0)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=124.18, default_y=-171.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=152.37, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.57, default_y=-116.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.76, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.96, default_y=-101.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=265.16, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=293.35, default_y=-156.85):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=321.55, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=357.85, default_y=-111.85):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=386.05, default_y=-121.85):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=414.24, default_y=-101.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=450.55, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='7', width=343.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=13.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=119.77, default_y=-10.0):
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
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-58.66)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-58.66)
                Staff(1)
            with Note(default_x=172.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=235.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=262.05, default_y=-5.0):
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
            with Note(default_x=288.55, default_y=-10.0):
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
            with Note(default_x=315.04, default_y=-5.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=13.8, default_y=-171.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=40.29, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=66.79, default_y=-116.85):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.28, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.77, default_y=-101.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.27, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=172.76, default_y=-156.85):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=199.25, default_y=-136.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.56, default_y=-111.85):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=262.05, default_y=-121.85):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=288.55, default_y=-96.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.04, default_y=-141.85):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='8', width=391.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=44.44)
            with Note(default_x=10.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-23.99):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=200.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.68, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=263.24, default_y=25.0):
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
            with Note(default_x=295.31, default_y=10.0):
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
            with Note(default_x=314.18, default_y=20.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(6)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue564', relative_x=-8.23, relative_y=45.81, font_family='MScore Text', font_size='15')
                Staff(1)
            with Note(default_x=331.87, default_y=15.0):
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
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=358.44, default_y=5.0):
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
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=10.72, default_y=-161.85):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.29, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.85, default_y=-116.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=105.42, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.98, default_y=-96.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.55, default_y=-116.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=200.11, default_y=-146.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=231.68, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.24, default_y=-101.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.31, default_y=-111.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=331.87, default_y=-91.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=358.44, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=333.82):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-57.66)
                Staff(1)
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=63.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=116.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=170.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-57.74, relative_x=-1.33)
                Staff(1)
            with Note(default_x=223.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=252.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=278.78, default_y=-5.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=29.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=305.5, default_y=-15.0):
                with Pitch():
                    Step('C')
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
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=10.0, default_y=-146.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=36.72, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=63.45, default_y=-101.85):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.17, default_y=-111.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=116.89, default_y=-91.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=143.62, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=170.34, default_y=-146.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=197.06, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.79, default_y=-96.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.05, default_y=-116.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=278.78, default_y=-91.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=305.5, default_y=-126.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='10', width=654.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(178.01)
                with StaffLayout(number=2):
                    StaffDistance(81.59)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=242.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=303.01, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=328.2, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=367.48, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=399.54, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=437.06, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-56.33)
                Staff(1)
            with Note(default_x=462.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=500.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=525.81, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=563.33, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=588.52, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=627.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(131.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(11)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.52)
                Staff(2)
            with Note(default_x=120.74, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.12, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.5, default_y=-106.59):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.87, default_y=-116.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.25, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=272.63, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
            with Note(default_x=303.01, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=351.81, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=421.22, default_y=-106.59):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=481.44, default_y=-116.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=541.65, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=604.19, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=599.41):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legatissimo', default_y=-40.0, relative_x=32.01, relative_y=-6.34, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.33)
                Staff(1)
            with Note(default_x=10.0, default_y=0.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccatissimo()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=67.59)
                Staff(1)
            with Note(default_x=39.91, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(7)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=77.3, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=111.77, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=141.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.07, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
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
            with Note(default_x=208.98, default_y=15.0):
                with Pitch():
                    Step('B')
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=238.89, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=276.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
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
            with Note(default_x=306.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=336.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
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
            with Note(default_x=373.48, default_y=-10.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=403.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.34, relative_y=-19.99):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=433.31, default_y=-20.0):
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
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=470.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-53.66)
                Staff(1)
            with Note(default_x=500.6, default_y=5.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=530.51, default_y=0.0):
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
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=567.9, default_y=-15.0):
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
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=10.0, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.6, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=111.77, default_y=-106.59):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.37, default_y=-116.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.98, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.58, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.52)
                Staff(2)
            with Note(default_x=306.19, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=354.79, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.4, default_y=-101.59):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=452.0, default_y=-121.59):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=500.6, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=549.21, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='12', width=294.9):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-60.21)
                Staff(1)
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=10.67)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-48.11, relative_y=-19.99):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=104.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-53.66)
                Staff(1)
            with Note(default_x=152.01, default_y=15.0):
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
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=199.11, default_y=15.0):
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
                        Staccato()
            with Note(default_x=246.21, default_y=15.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.52)
                Staff(2)
            with Note(default_x=10.72, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=34.27, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.82, default_y=-106.59):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.37, default_y=-116.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=104.92, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.46, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=152.01, default_y=-151.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=175.56, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.11, default_y=-106.59):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.66, default_y=-116.59):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.21, default_y=-96.59):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.75, default_y=-131.59):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='13', width=524.98):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.41)
                with StaffLayout(number=2):
                    StaffDistance(79.79)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=124.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=253.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=318.44, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=383.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=415.39, default_y=-5.0):
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
            with Note(default_x=447.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(360.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=500.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.02)
                Staff(2)
            with Note(default_x=124.54, default_y=-149.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.86, default_y=-129.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=189.17, default_y=-104.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.49, default_y=-114.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.8, default_y=-84.79):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=286.12, default_y=-114.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=318.44, default_y=-134.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=350.75, default_y=-124.79):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=383.07, default_y=-99.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=415.39, default_y=-114.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.7, default_y=-89.79):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=480.02, default_y=-99.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
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
        with Measure(number='14', width=543.22):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-57.66)
                Staff(1)
            with Note(default_x=10.36, default_y=0.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-42.67, relative_y=-19.99):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=144.17, default_y=-5.0):
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
            with Note(default_x=178.96, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=194.93, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-56.33)
                Staff(1)
            with Note(default_x=210.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=242.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=288.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=354.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=402.71, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=450.05, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=504.9, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.72, default_y=-144.79):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=44.08, default_y=-124.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=77.45, default_y=-99.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=110.81, default_y=-109.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.17, default_y=-79.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=177.53, default_y=-109.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=210.89, default_y=-129.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=258.28, default_y=-109.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=326.79, default_y=-144.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=378.43, default_y=-159.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=430.06, default_y=-134.79):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=479.77, default_y=-144.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='15', width=480.7):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-50.67):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('appassionato', default_y=-40.0, relative_y=-19.66, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=13.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=156.36, default_y=15.0):
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
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=187.03, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=223.48, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=252.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=408.0, default_y=-15.0):
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
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=14.16, default_y=-149.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.71, default_y=-129.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.26, default_y=-104.79):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.81, default_y=-114.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.36, default_y=-134.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=205.26, default_y=-89.79):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=252.63, default_y=-164.79):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=304.71, default_y=-129.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=336.9, default_y=-114.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.45, default_y=-94.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=408.0, default_y=-99.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=443.55, default_y=-119.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1680.0)
            with Note(default_x=287.82, default_y=-129.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='16', width=629.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.41)
                with StaffLayout(number=2):
                    StaffDistance(66.09)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-63.99)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-63.99)
                Staff(1)
            with Note(default_x=120.38, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=143.82, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=255.68, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=292.97, default_y=15.0):
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=323.64, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=361.86, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=392.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=553.02, default_y=-15.0):
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
            with Note(default_x=613.08, default_y=-20.0, print_object='no'):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('none')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=143.82, default_y=-136.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=181.11, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.39, default_y=-91.09):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.68, default_y=-101.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.97, default_y=-121.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=342.75, default_y=-76.09):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.04)
                Staff(2)
            with Note(default_x=392.44, default_y=-151.09):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=446.26, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=478.45, default_y=-101.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=515.74, default_y=-81.09):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.02, default_y=-86.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=590.31, default_y=-106.09):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1680.0)
            with Note(default_x=429.37, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='17', width=544.13):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_y=-23.99):
                        OtherDynamics('con forza')
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=56.33)
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.44, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=109.82, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=141.14, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    with Articulations():
                        Staccato()
            with Note(default_x=180.29, default_y=5.0):
                with Pitch():
                    Step('G')
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=211.61, default_y=25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccato()
            with Note(default_x=242.93, default_y=15.0):
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
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=282.08, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=313.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-19.99):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=466.15, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.01)
                Staff(2)
            with Note(default_x=33.44, default_y=-146.09):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=71.63, default_y=-126.09):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.82, default_y=-111.09):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.72, default_y=-101.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.61, default_y=-81.09):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=262.5, default_y=-111.09):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.04)
                Staff(2)
            with Note(default_x=313.4, default_y=-121.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=351.59, default_y=-111.09):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=389.78, default_y=-96.09):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=427.97, default_y=-86.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=466.15, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=504.34, default_y=-86.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(2400.0)
            with Note(default_x=466.15, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='18', width=375.57):
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
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
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-73.63)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-100.04)
                Staff(2)
            with Note(default_x=10.72, default_y=-136.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=40.99, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.26, default_y=-91.09):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.53, default_y=-101.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.81, default_y=-81.09):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.08, default_y=-91.09):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-51.65, relative_y=-40.0):
                        Mf()
                Staff(2)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-89.43)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-89.43)
                Staff(2)
            with Note(default_x=192.35, default_y=-101.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.62, default_y=-116.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=252.89, default_y=-126.09):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.16, default_y=-136.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=313.43, default_y=-151.09):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=1.33)
                Staff(2)
            with Note(default_x=343.7, default_y=-156.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(2)
        with Measure(number='19', width=604.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(145.41)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    Words('sotto voce', default_y=69.27, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Note(default_x=123.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=363.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=363.26, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=124.18, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=164.08, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.99, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=323.71, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=363.62, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=403.52, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.43, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.34, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.24, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=563.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='20', width=476.8):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=52.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=52.25, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=90.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=90.7, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=167.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=167.6, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=244.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=244.5, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=321.04, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=321.04, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-107.7)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=52.25, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.7, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.15, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.6, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.05, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=244.5, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=282.95, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=321.4, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=359.85, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=398.3, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=436.75, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='21', width=467.44):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=88.78, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=88.78, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-74.47)
                Staff(1)
            with Note(default_x=239.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=239.82, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=22.67)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=314.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=314.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.47, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=89.14, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=126.81, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.48, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=239.82, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=277.49, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=315.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=352.83, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=390.5, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.17, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='22', width=545.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(68.45)
            with Note(default_x=124.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.18, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.19, default_y=-30.0):
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
            with Note(default_x=159.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=194.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=194.21, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=264.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=264.24, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=333.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=333.91, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=124.18, default_y=-163.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.19, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.21, default_y=-123.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.22, default_y=-108.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.24, default_y=-133.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.25, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=334.27, default_y=-163.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=369.28, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.3, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=439.31, default_y=-108.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=474.33, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=509.34, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='23', width=498.32):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.16, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rallent.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-85.6)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-85.6)
                Staff(1)
            with Note(default_x=13.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.44, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=254.9, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.9, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-163.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.04, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.29, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.53, default_y=-108.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.77, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.02, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.0)
                Staff(2)
            with Note(default_x=255.26, default_y=-168.45):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=295.51, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=335.75, default_y=-133.45):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.99, default_y=-113.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=416.24, default_y=-133.45):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=456.48, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.53, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=108.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=100.0)
        with Measure(number='24', width=504.62):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=5.34, relative_y=-45.6):
                        Ppp()
                Staff(1)
                Sound(dynamics=53.33)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Staff(1)
                Sound(tempo=96.0)
            with Note(default_x=17.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=58.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=58.24, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=98.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.54, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=179.54, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.78, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=260.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=260.05, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=17.8, default_y=-163.45):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.24, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.67, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.11, default_y=-118.45):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.54, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.98, default_y=-143.45):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=260.41, default_y=-163.45):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=300.85, default_y=-148.45):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=341.28, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.72, default_y=-113.45):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=422.15, default_y=-128.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=462.59, default_y=-148.45):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=92.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=84.0)
        with Measure(number='25', width=637.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(125.93)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=132.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=132.98, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=174.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.93, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=216.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=216.88, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=300.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=300.77, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=1.7, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=116.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.25, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=384.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=384.31, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=132.98, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.93, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.82, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.72, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=384.67, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=426.62, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=468.57, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=510.51, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=552.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=594.41, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=76.0)
        with Measure(number='26', width=468.89):
            with Note(default_x=15.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=241.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=241.39, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=31.63)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=31.63)
                Staff(2)
            with Note(default_x=16.2, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.38, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.97, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.16, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.67)
                Staff(2)
            with Note(default_x=241.75, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=279.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.93, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=354.52, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=392.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=11.0, relative_y=30.0):
                        Ff()
                Staff(2)
                Sound(dynamics=120.0)
            with Note(default_x=429.7, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='27', width=442.05):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=13.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.44, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=226.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=226.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=49.29, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.77, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.26, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=155.74, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=226.72, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=262.2, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.69, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=333.99, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=369.48, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=404.97, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='28', width=594.37):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=124.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=124.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=163.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=163.23, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=202.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=202.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=280.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=280.38, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=358.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=358.48, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=436.21, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=436.21, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-107.7)
                Staff(2)
            with Note(default_x=124.18, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=163.23, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.28, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.33, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.38, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=319.43, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=358.48, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=397.53, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=436.57, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=475.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=514.67, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.72, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='29', width=474.63):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=89.98, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=89.98, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=243.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=243.42, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=319.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=319.6, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.07, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.34, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.61, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.88, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.15, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=243.42, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=281.69, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=319.96, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=358.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.5, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=434.77, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='30', width=479.9):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=52.51, default_y=-30.0):
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
            with Note(default_x=52.51, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.22, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=91.22, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue564', relative_x=63.25, relative_y=34.32, font_family='MScore Text', font_size='15')
                Staff(1)
            with Note(default_x=168.63, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=168.63, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=228.0, default_y=-25.0):
                Grace()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=228.0, default_y=10.0):
                Grace()
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=245.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=245.69, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.51, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.22, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.92, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.63, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=246.05, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=284.76, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=323.47, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=362.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=400.88, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=439.59, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='31', width=574.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(68.67)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.74, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rallent.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-85.6)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-85.6)
                Staff(1)
            with Note(default_x=123.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=123.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=348.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=348.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=124.18, default_y=-163.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.57, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=198.96, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.36, default_y=-108.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.75, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=311.14, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.0)
                Staff(2)
            with Note(default_x=348.54, default_y=-168.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=385.93, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=423.32, default_y=-133.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=460.72, default_y=-113.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=498.11, default_y=-133.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=535.5, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.06, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=108.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=100.0)
        with Measure(number='32', width=470.42):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=5.34, relative_y=-45.6):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.81, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Staff(1)
                Sound(tempo=96.0)
            with Note(default_x=17.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=55.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=55.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=92.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=92.97, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=168.14, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=168.14, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=242.95, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=242.95, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=17.8, default_y=-163.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.38, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.97, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.55, default_y=-118.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.14, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.72, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=243.31, default_y=-163.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=280.89, default_y=-148.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=318.48, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=356.06, default_y=-113.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=393.65, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=431.23, default_y=-148.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=92.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=84.0)
        with Measure(number='33', width=504.0):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=17.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=58.18, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=58.18, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=98.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=98.57, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=179.33, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.33, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.25, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=1.7, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=116.0)
            with Note(default_x=259.74, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=259.74, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=17.8, default_y=-163.67):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.18, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.57, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.95, default_y=-118.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.33, default_y=-128.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.72, default_y=-143.67):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=260.1, default_y=-148.67):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=300.48, default_y=-133.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=340.86, default_y=-123.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.25, default_y=-103.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=421.63, default_y=-123.67):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=462.01, default_y=-133.67):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=76.0)
        with Measure(number='34', width=639.74):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(78.08)
            with Note(default_x=131.22, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.22, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=384.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=384.5, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=131.58, default_y=-153.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.8, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.01, default_y=-123.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.22, default_y=-113.08):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=300.44, default_y=-118.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=342.65, default_y=-153.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=384.86, default_y=-173.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=427.07, default_y=-153.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=469.29, default_y=-138.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=511.5, default_y=-118.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=553.71, default_y=-138.08):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=595.93, default_y=-148.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='35', width=449.56):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.0, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-18.67, relative_y=-28.28):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco stretto', default_y=-40.4, relative_x=9.34, relative_y=-52.47, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=27.92, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('122')
                Staff(1)
                Sound(tempo=122.0)
            with Note(default_x=228.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=228.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=10.36, default_y=-153.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=46.83, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.29, default_y=-118.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.76, default_y=-108.08):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.23, default_y=-118.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.7, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=229.16, default_y=-153.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=265.63, default_y=-138.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.1, default_y=-128.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.56, default_y=-113.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=375.03, default_y=-128.08):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=411.5, default_y=-138.08):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='36', width=459.6):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-74.52, relative_x=2.67)
                Staff(1)
            with Note(default_x=84.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=84.67, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=122.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=122.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=159.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=159.33, default_y=10.0):
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
            with Note(default_x=196.67, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.67, default_y=15.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-14.67)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-50.78, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=234.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=234.0, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=308.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.67, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=383.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=383.34, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-158.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.33, default_y=-148.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.67, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.0, default_y=-113.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.33, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.67, default_y=-148.08):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=234.0, default_y=-158.08):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=271.33, default_y=-143.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=308.67, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=346.0, default_y=-118.08):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=383.34, default_y=-133.08):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=420.67, default_y=-143.08):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='37', width=553.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(72.91)
            with Note(default_x=124.18, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-74.45)
                Staff(1)
            with Note(default_x=195.53, default_y=-20.0):
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
            with Note(default_x=195.53, default_y=15.0):
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
            with Note(default_x=231.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=231.21, default_y=10.0):
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
            with Note(default_x=266.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=266.88, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=302.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.56, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-16.01)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.95, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=338.24, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=338.24, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-55.65, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.78)
                Staff(1)
            with Note(default_x=409.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=409.59, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=445.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=445.26, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=480.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=480.94, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=17.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-63.93, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=516.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=516.62, default_y=-10.0):
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
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.5)
                Staff(2)
            with Note(default_x=124.18, default_y=-157.91):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.85, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.53, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.21, default_y=-112.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.88, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=302.56, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=338.24, default_y=-167.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=373.91, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.59, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=445.26, default_y=-112.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=480.94, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=516.62, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='38', width=493.7):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.48, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1920.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.48, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1920.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.22)
                Staff(1)
            with Note(default_x=332.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=332.66, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=13.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-50.7, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=412.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=412.38, default_y=-5.0):
                Chord()
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
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-167.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-10.67, relative_y=32.67):
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Note(default_x=53.66, default_y=-142.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=93.52, default_y=-127.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.37, default_y=-117.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.23, default_y=-127.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.09, default_y=-142.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=252.95, default_y=-167.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=292.81, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=332.66, default_y=-137.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=372.52, default_y=-117.91):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=412.38, default_y=-137.91):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=452.24, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='39', width=501.32):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.2, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rallent.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-87.35)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-87.35)
                Staff(1)
            with Note(default_x=13.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.44, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=256.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.4, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-167.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=54.29, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.79, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.28, default_y=-112.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.77, default_y=-132.91):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=216.27, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.0)
                Staff(2)
            with Note(default_x=256.76, default_y=-172.91):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=297.25, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=337.74, default_y=-137.91):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=378.24, default_y=-117.91):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=418.73, default_y=-137.91):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=459.22, default_y=-147.91):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=15.57, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=108.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=100.0)
        with Measure(number='40', width=581.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(79.2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=5.34, relative_y=-45.6):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.81, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Staff(1)
                Sound(tempo=96.0)
            with Note(default_x=132.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=132.98, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=170.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=170.2, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=207.43, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=207.43, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=281.88, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=281.88, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.78, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=355.98, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=355.98, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=132.98, default_y=-174.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=170.2, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.43, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=244.66, default_y=-129.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=281.88, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=319.11, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=356.34, default_y=-174.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=393.56, default_y=-159.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=430.79, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=468.02, default_y=-124.2):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=505.24, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=542.47, default_y=-159.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=92.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=84.0)
        with Measure(number='41', width=499.7):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=17.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=57.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=57.82, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=97.85, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=97.85, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=177.9, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=177.9, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.2, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=1.7, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=116.0)
            with Note(default_x=257.59, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=257.59, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-107.7)
                Staff(2)
            with Note(default_x=17.8, default_y=-174.2):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=57.82, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.85, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.87, default_y=-129.2):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.9, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.92, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=257.95, default_y=-159.2):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=297.97, default_y=-144.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=338.0, default_y=-134.2):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=378.02, default_y=-114.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=418.05, default_y=-134.2):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=458.07, default_y=-144.2):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=76.0)
        with Measure(number='42', width=467.91):
            with Note(default_x=15.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=240.89, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=240.89, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=16.2, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=53.71, default_y=-134.2):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.22, default_y=-124.2):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.73, default_y=-114.2):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.24, default_y=-119.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.75, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=241.26, default_y=-174.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=278.76, default_y=-154.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.27, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=353.78, default_y=-119.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=391.29, default_y=-139.2):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.8, default_y=-149.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='43', width=583.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(122.9)
                with StaffLayout(number=2):
                    StaffDistance(70.96)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=120.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=351.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=351.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=120.74, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.18, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.61, default_y=-110.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=236.05, default_y=-100.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.48, default_y=-110.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.92, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=351.36, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=389.79, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.23, default_y=-120.96):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=466.67, default_y=-105.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=505.1, default_y=-120.96):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=543.54, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='44', width=483.24):
            with Note(default_x=10.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.0, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-74.52, relative_x=2.67)
                Staff(1)
            with Note(default_x=88.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=88.61, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.91, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=167.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.21, default_y=10.0):
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
            with Note(default_x=206.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=206.51, default_y=15.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-14.67)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-50.78, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=245.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=245.82, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=324.42, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=324.42, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=403.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=403.03, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=10.0, default_y=-150.96):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.3, default_y=-140.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.61, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=127.91, default_y=-105.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=167.21, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.51, default_y=-140.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=245.82, default_y=-150.96):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=285.12, default_y=-135.96):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=324.42, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=363.73, default_y=-110.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=403.03, default_y=-125.96):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.33, default_y=-135.96):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='45', width=482.1):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-74.45)
                Staff(1)
            with Note(default_x=91.58, default_y=-20.0):
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
            with Note(default_x=91.58, default_y=15.0):
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
            with Note(default_x=130.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.47, default_y=10.0):
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
            with Note(default_x=169.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=169.37, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=208.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=208.26, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=-16.01)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-46.95, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=247.15, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=247.15, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-55.49, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.78)
                Staff(1)
            with Note(default_x=324.93, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=324.93, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=363.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=363.82, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=402.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=402.71, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=17.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-63.92, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=441.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=441.6, default_y=-10.0):
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
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-155.96):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.69, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.58, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.47, default_y=-110.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.37, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.26, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=247.15, default_y=-165.96):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=286.04, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=324.93, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=363.82, default_y=-110.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=402.71, default_y=-130.96):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=441.6, default_y=-145.96):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='46', width=582.71):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(74.49)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=120.86, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1920.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=120.86, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1920.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-79.22)
                Staff(1)
            with Note(default_x=428.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=428.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=13.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-44.22, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=504.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=504.95, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=124.18, default_y=-169.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, relative_x=-10.7, relative_y=34.03):
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Note(default_x=162.26, default_y=-144.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=200.33, default_y=-129.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=238.41, default_y=-119.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.49, default_y=-129.49):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.57, default_y=-144.49):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=352.64, default_y=-169.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=390.72, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=428.8, default_y=-139.49):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=466.87, default_y=-119.49):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=504.95, default_y=-139.49):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=543.03, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='47', width=479.95):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.7, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('poco rallent.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-93.58)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-93.58)
                Staff(1)
            with Note(default_x=13.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=13.44, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=10.95, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=245.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=245.71, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-169.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.51, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.22, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.94, default_y=-114.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.65, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.36, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-116.0)
                Staff(2)
            with Note(default_x=246.07, default_y=-174.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=284.79, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=323.5, default_y=-139.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=362.21, default_y=-119.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=400.92, default_y=-139.49):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=439.64, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=108.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=100.0)
        with Measure(number='48', width=486.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-47.98, relative_x=5.34, relative_y=-45.6):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Staff(1)
                Sound(tempo=96.0)
            with Note(default_x=17.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=56.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=56.7, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=95.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=95.61, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=173.42, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=173.42, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=14.78, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('88')
                Staff(1)
                Sound(tempo=88.0)
            with Note(default_x=250.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=250.86, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=17.8, default_y=-169.49):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.7, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.61, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=134.51, default_y=-124.49):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.42, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.32, default_y=-149.49):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=251.22, default_y=-169.49):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=290.13, default_y=-154.49):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=329.03, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=367.94, default_y=-119.49):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=406.84, default_y=-134.49):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=445.75, default_y=-154.49):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=92.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Offset(-720.0)
                Staff(1)
                Sound(tempo=84.0)
        with Measure(number='49', width=632.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(115.28)
                with StaffLayout(number=2):
                    StaffDistance(76.31)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=12.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=132.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=132.98, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=174.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=174.47, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=215.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=215.96, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=298.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=298.94, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-53.25, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='above'):
                with DirectionType():
                    Words('a tempo', default_y=1.7, relative_y=20.0, font_weight='bold', font_style='italic', font_size='12')
                Staff(1)
                Sound(tempo=116.0)
            with Note(default_x=381.56, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=381.56, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-107.7)
                Staff(2)
            with Note(default_x=132.98, default_y=-171.31):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=174.47, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=215.96, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.45, default_y=-126.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.94, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=340.43, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=381.92, default_y=-156.31):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=423.41, default_y=-141.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=464.9, default_y=-131.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=506.39, default_y=-111.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=547.88, default_y=-131.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=589.37, default_y=-141.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('76')
                Offset(-2160.0)
                Staff(1)
                Sound(tempo=76.0)
        with Measure(number='50', width=485.5):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-98.33)
                Staff(1)
            with Note(default_x=15.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=15.84, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=249.69, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=249.69, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
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
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-88.5)
                Staff(2)
            with Note(default_x=16.2, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.17, default_y=-131.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.15, default_y=-121.31):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.12, default_y=-111.31):
                with Pitch():
                    Step('B')
                    Alter(-2.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat-flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=172.1, default_y=-116.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.07, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=250.05, default_y=-171.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=289.02, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=328.0, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=366.97, default_y=-116.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=405.95, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=444.92, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='51', width=430.94):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.95, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=16.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=154.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=188.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=222.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=360.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Note(default_x=16.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=16.56, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=222.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=222.77, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=16.92, default_y=-171.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.29, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.66, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=120.03, default_y=-116.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.4, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.76, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=223.13, default_y=-171.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=257.5, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=291.87, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=326.24, default_y=-116.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.61, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=394.98, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
        with Measure(number='52', width=592.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(127.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=131.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=131.58, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=246.37, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=246.37, default_y=15.0):
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
            with Note(default_x=284.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=284.64, default_y=10.0):
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
            with Note(default_x=322.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=322.9, default_y=15.0):
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
            with Note(default_x=361.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=361.16, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=131.58, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.85, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=246.37, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=284.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=322.9, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=361.16, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=399.43, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=437.69, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=475.95, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=514.22, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=552.48, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='53', width=454.43):
            with Note(default_x=22.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=166.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=237.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=381.17, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Note(default_x=19.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Note(default_x=19.52, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1920.0)
                Voice('2')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Note(default_x=309.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=309.14, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=22.84, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=58.67, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.51, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.34, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.17, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=202.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=237.84, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=273.67, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=309.5, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=345.33, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.17, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=417.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='54', width=502.13):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=16.2, default_y=10.0):
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
            with Note(default_x=56.56, default_y=-10.0):
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
            with Note(default_x=56.56, default_y=15.0):
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
            with Note(default_x=96.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.92, default_y=10.0):
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
            with Note(default_x=137.28, default_y=-10.0):
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
            with Note(default_x=137.28, default_y=15.0):
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
            with Note(default_x=177.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.64, default_y=10.0):
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
            with Note(default_x=218.0, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=218.0, default_y=15.0):
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
            with Note(default_x=258.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=258.0, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=16.2, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.56, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.92, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.28, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=218.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=258.36, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=298.73, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=339.09, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=419.81, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=460.17, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='55', width=604.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(127.26)
                with StaffLayout(number=2):
                    StaffDistance(68.56)
            with Direction(placement='below'):
                with DirectionType():
                    Words('con forza', default_y=-53.09, relative_y=-35.0, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-58.99)
                Staff(1)
            with Note(default_x=124.18, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=124.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=243.92, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=243.92, default_y=30.0):
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
            with Note(default_x=283.83, default_y=10.0):
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
            with Note(default_x=283.83, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=323.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=323.75, default_y=10.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=363.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=363.3, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=523.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=523.32, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=523.32, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=124.18, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=164.09, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=204.01, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.92, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=283.83, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=323.75, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=363.66, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=403.58, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=443.49, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=483.4, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.32, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=563.23, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='56', width=465.55):
            with Note(default_x=22.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=22.48, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=243.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.03, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Note(default_x=19.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(2880.0)
                Voice('2')
                Type('whole')
                Dot()
                Accidental('flat')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=22.84, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.6, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.36, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.12, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.88, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.64, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=243.4, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=280.15, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=316.91, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=353.67, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=390.43, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=427.19, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='57', width=478.61):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=129.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=129.6, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=168.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.2, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=206.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=206.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=245.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=245.04, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=399.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(2400.0)
            with Note(default_x=399.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=399.81, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=13.8, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=52.4, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.0, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=129.6, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.2, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.8, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.5)
                Staff(2)
            with Note(default_x=245.4, default_y=-163.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=284.01, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=322.61, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=361.21, default_y=-108.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=399.81, default_y=-128.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=438.41, default_y=-143.56):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='58', width=478.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(134.95)
                with StaffLayout(number=2):
                    StaffDistance(70.24)
            with Note(default_x=127.14, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=127.14, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=301.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=301.91, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Note(default_x=124.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(2880.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-108.51)
                Staff(2)
            with Note(default_x=127.5, default_y=-165.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.63, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.76, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.88, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=244.01, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.14, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=302.27, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=331.4, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=360.53, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=389.65, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=418.78, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=447.91, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='59', width=356.2):
            with Note():
                Rest(measure='yes')
                Duration(2880.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=10.0, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=38.72, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.43, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.15, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.87, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.58, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=182.3, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=211.02, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.73, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.45, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.17, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=325.88, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='60', width=356.2):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest(measure='yes')
                Duration(2880.0)
                Voice('1')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=10.0, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.72, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.43, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.15, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=124.87, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.58, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=182.3, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=211.02, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.73, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.45, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.17, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=325.88, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='61', width=357.86):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=-4.34, relative_y=-39.22):
                        Ppp()
                        OtherDynamics(' legatissimo')
                Staff(1)
                Sound(dynamics=50.0)
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=10.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=125.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.9, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=154.7, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=154.7, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=183.13, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=183.13, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=298.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=298.67, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=10.72, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.52, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.31, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=97.11, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=125.9, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.7, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=183.49, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=212.29, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.08, default_y=-95.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=269.88, default_y=-110.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=298.67, default_y=-130.24):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=327.47, default_y=-145.24):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='62', width=590.44):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(127.26)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=124.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.18, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=240.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=240.34, default_y=15.0):
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
            with Note(default_x=279.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=279.07, default_y=10.0):
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
            with Note(default_x=317.79, default_y=5.0):
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
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=317.79, default_y=15.0):
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
            with Note(default_x=356.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=356.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.52)
                Staff(2)
            with Note(default_x=124.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.9, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=201.62, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=240.34, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=279.07, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=317.79, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-85.52)
                Staff(2)
            with Note(default_x=356.51, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=395.23, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=433.96, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=472.68, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=511.4, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=550.12, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='63', width=448.29):
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=10.36, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=156.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=156.04, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=192.37, default_y=-10.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=192.37, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=228.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=228.34, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=374.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=374.03, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.62)
                Staff(2)
            with Note(default_x=10.72, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.05, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=119.71, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=156.04, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.37, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-85.62)
                Staff(2)
            with Note(default_x=228.7, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=265.03, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=301.36, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=337.7, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=374.03, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=410.36, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='64', width=510.18):
            with Note(default_x=13.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=10.0):
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
            with Note(default_x=55.03, default_y=5.0):
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
            with Note(default_x=55.03, default_y=15.0):
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
            with Note(default_x=96.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.26, default_y=10.0):
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
            with Note(default_x=137.49, default_y=5.0):
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
            with Note(default_x=137.49, default_y=15.0):
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
            with Note(default_x=178.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=178.73, default_y=10.0):
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
            with Note(default_x=219.96, default_y=5.0):
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
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=219.96, default_y=15.0):
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
            with Note(default_x=260.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=260.83, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-85.42)
                Staff(2)
            with Note(default_x=13.8, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=55.03, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.26, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.49, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.73, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.96, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-85.42)
                Staff(2)
            with Note(default_x=261.19, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=302.42, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=343.65, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=426.11, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=467.34, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='65', width=472.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(116.88)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_y=-40.0, relative_x=-1.89, relative_y=-22.07):
                        OtherDynamics('sempre pianissimo')
                Staff(1)
                Sound(dynamics=60.0)
            with Note(default_x=124.18, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.18, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=210.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=210.88, default_y=30.0):
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
            with Note(default_x=239.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.78, default_y=25.0):
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
            with Note(default_x=268.68, default_y=0.0):
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
            with Note(default_x=268.68, default_y=10.0):
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
            with Note(default_x=297.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=297.22, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=413.18, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=413.18, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=124.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=153.08, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.98, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.88, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=239.78, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.68, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.2)
                Staff(2)
            with Note(default_x=297.58, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=326.48, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=355.38, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=384.28, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=413.18, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.08, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='66', width=341.87):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=176.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=176.85, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.39)
                Staff(2)
            with Note(default_x=14.16, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.34, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.51, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.69, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.86, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.04, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-86.39)
                Staff(2)
            with Note(default_x=177.21, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=204.39, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=231.57, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.74, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.92, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=313.09, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
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
        with Measure(number='67', width=390.11):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-34.66):
                        Fz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2880.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=13.32, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2880.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-110.34)
                Staff(2)
            with Note(default_x=16.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-41.25, relative_y=-40.0):
                        OtherDynamics('sempre ')
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Note(default_x=47.63, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=78.62, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.61, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=140.6, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.59)
                Staff(2)
            with Note(default_x=171.59, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=202.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=233.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.55, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=295.54, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=326.53, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.13)
                Staff(2)
            with Note(default_x=357.52, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='68', width=344.35):
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-65.33)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-65.33)
                Staff(1)
            with Note(default_x=13.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2880.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=13.32, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2880.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=66.67)
            with Note(default_x=16.64, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.82, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=70.99, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=125.34, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.13)
                Staff(2)
            with Note(default_x=152.52, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=179.69, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=206.87, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=234.05, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=261.22, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=288.4, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.13)
                Staff(2)
            with Note(default_x=315.57, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='69', width=579.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(127.26)
                with StaffLayout(number=2):
                    StaffDistance(70.82)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2880.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=120.38, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2880.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                Dot()
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Note(default_x=123.7, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.51, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.32, default_y=-95.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=237.13, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=274.94, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.57)
                Staff(2)
            with Note(default_x=312.75, default_y=-145.82):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=350.56, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=388.37, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=426.18, default_y=-95.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=463.99, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=501.79, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-93.57)
                Staff(2)
            with Note(default_x=539.6, default_y=-145.82):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='70', width=506.92):
            with Note():
                Rest()
                Duration(960.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('rall. e dolciss.', default_y=-40.0, relative_y=-25.66, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Staff(1)
                Sound(tempo=108.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=40.76, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=257.66, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=298.93, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=41.4, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Staff(1)
                Sound(tempo=92.0)
            with Note(default_x=340.21, default_y=25.0):
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
            with Note(default_x=381.49, default_y=10.0):
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
                with Notations():
                    with Articulations():
                        Accent()
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=35.25, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('84')
                Staff(1)
                Sound(tempo=84.0)
            with Note(default_x=422.76, default_y=15.0):
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
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=464.04, default_y=5.0):
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
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=0.75, relative_y=30.0):
                        Pp()
                Staff(2)
                Sound(dynamics=50.0)
            with Note(default_x=10.0, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=51.28, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=92.55, default_y=-95.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.83, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=175.11, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=216.38, default_y=-140.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=257.66, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=298.93, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=340.21, default_y=-95.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=381.49, default_y=-105.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=422.76, default_y=-85.82):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=464.04, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1200.0)
            with Note(default_x=216.38, default_y=-140.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(480.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1680.0)
            with Forward():
                Duration(1440.0)
            with Note(default_x=257.66, default_y=-130.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('7')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(1920.0)
            with Forward():
                Duration(1680.0)
            with Note(default_x=298.93, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('8')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(720.0)
        with Measure(number='71', width=462.98):
            with Direction(placement='above'):
                with DirectionType():
                    Words('Tempo I', default_y=23.25, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=116.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=85.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=160.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=235.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=310.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=348.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=386.15, default_y=-5.0):
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
            with Note(default_x=423.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-76.31)
                Staff(2)
            with Note(default_x=10.0, default_y=-140.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=47.61, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.23, default_y=-95.82):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.84, default_y=-105.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.46, default_y=-85.82):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=198.07, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=235.69, default_y=-140.82):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=273.3, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=310.92, default_y=-90.82):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=348.53, default_y=-110.82):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=386.15, default_y=-85.82):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=423.76, default_y=-120.82):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='72', width=574.47):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(74.43)
                with StaffLayout(number=2):
                    StaffDistance(77.56)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=263.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=334.93, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=370.63, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=406.33, default_y=25.0):
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
            with Note(default_x=442.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=477.72, default_y=20.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=507.0, default_y=15.0):
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
                Beam('continue', number=1)
            with Note(default_x=543.59, default_y=5.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=120.74, default_y=-147.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=156.44, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=192.14, default_y=-102.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.83, default_y=-112.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.53, default_y=-92.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=299.23, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
            with Note(default_x=334.93, default_y=-147.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=370.63, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=406.33, default_y=-102.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=442.02, default_y=-112.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=477.72, default_y=-92.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=525.3, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='73', width=974.44):
            with Note(default_x=10.0, default_y=0.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=45.74, default_y=5.0):
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
            with Note(default_x=100.99, default_y=-5.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=136.73, default_y=0.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('legatissimo', default_y=-40.0, relative_y=-24.33, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=66.43)
                Staff(1)
            with Note(default_x=172.47, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(7)
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=227.72, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=263.45, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=299.19, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(160.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=354.44, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(7)
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
            with Note(default_x=390.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=422.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=448.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=475.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=512.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=541.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=567.59, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=604.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=631.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=657.96, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=684.35, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=710.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=737.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=763.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=800.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=827.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=853.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=891.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=920.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=946.45, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(72.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(20)
                    NormalNotes(6)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=10.0, default_y=-147.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=73.36, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.73, default_y=-102.56):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=200.09, default_y=-112.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.45, default_y=-92.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=326.82, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=390.18, default_y=-147.56):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=490.69, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=589.24, default_y=-97.56):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=684.35, default_y=-117.56):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=779.18, default_y=-92.56):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=875.52, default_y=-127.56):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='74', width=488.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(86.66)
            with Note(default_x=120.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-58.99)
                Staff(1)
            with Note(default_x=242.65, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=303.6, default_y=15.0):
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
                    Slur(type='stop', number=1)
            with Note(default_x=364.55, default_y=15.0):
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
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=425.51, default_y=15.0):
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
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=120.74, default_y=-156.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=151.22, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.69, default_y=-111.66):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=212.17, default_y=-121.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.65, default_y=-101.66):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=273.12, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=303.6, default_y=-156.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=334.08, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=364.55, default_y=-111.66):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=395.03, default_y=-121.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=425.51, default_y=-101.66):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=455.99, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='75', width=517.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-58.05)
                Staff(1)
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=18.67)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=147.7, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=214.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=246.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=291.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=338.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=387.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(206.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=434.96, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(309.0)
                Voice('1')
                Type('eighth')
                Dot()
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=492.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(103.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(7)
                    NormalNotes(6)
                    NormalType('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.02)
                Staff(2)
            with Note(default_x=14.16, default_y=-156.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=47.55, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.93, default_y=-111.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=114.31, default_y=-121.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=147.7, default_y=-91.66):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.08, default_y=-121.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=214.47, default_y=-141.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=261.88, default_y=-131.66):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=311.63, default_y=-106.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=363.29, default_y=-121.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=414.96, default_y=-96.66):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=464.71, default_y=-106.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
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
        with Measure(number='76', width=542.87):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-57.66)
                Staff(1)
            with Note(default_x=10.36, default_y=0.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=25.34)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=179.51, default_y=-5.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    Words('\ue261', relative_x=5.6, relative_y=41.4, font_family='MScore Text', font_size='13')
                Staff(1)
            with Note(default_x=263.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-52.33)
                Staff(1)
            with Note(default_x=367.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=409.29, default_y=10.0):
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
            with Note(default_x=451.49, default_y=15.0):
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
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1, relative_x=20.01)
                Staff(1)
            with Note(default_x=493.68, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(1440.0)
            with Note(default_x=263.9, default_y=0.0, print_object='no'):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('quarter', size='cue')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('none')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Tremolo(3, type='start')
            with Note(default_x=308.07, default_y=5.0, print_object='no'):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(240.0)
                Voice('2')
                Type('quarter', size='cue')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(2)
                    NormalNotes(1)
                Stem('none')
                Staff(1)
                with Notations():
                    with Ornaments():
                        Tremolo(3, type='stop')
            with Note(default_x=328.11, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=344.08, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('2')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(1920.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(2)
            with Note(default_x=10.72, default_y=-151.66):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.92, default_y=-131.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.11, default_y=-106.66):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.31, default_y=-116.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=179.51, default_y=-86.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=221.7, default_y=-116.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
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
                    Pedal(type='start', line='yes', default_y=-96.0)
                Staff(2)
            with Note(default_x=263.9, default_y=-136.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=306.1, default_y=-116.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=367.09, default_y=-151.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=409.29, default_y=-166.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=451.49, default_y=-141.66):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=493.68, default_y=-151.66):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
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
        with Measure(number='77', width=563.66):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(76.6)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-42.67):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=124.18, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=256.62, default_y=15.0):
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
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=287.3, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=321.15, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=347.87, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=496.01, default_y=-15.0):
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
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=124.54, default_y=-146.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.56, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=190.58, default_y=-101.6):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=223.6, default_y=-111.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=256.62, default_y=-131.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=304.22, default_y=-86.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=348.23, default_y=-161.6):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=397.78, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=429.97, default_y=-111.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=462.99, default_y=-91.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=496.01, default_y=-96.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=529.03, default_y=-116.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1680.0)
            with Note(default_x=380.89, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='78', width=482.44):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-63.99)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-63.99)
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=33.44, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(720.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.24, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=169.17, default_y=15.0):
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
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=199.84, default_y=5.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=234.63, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=262.1, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=412.97, default_y=-15.0):
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
            with Note(default_x=466.32, default_y=-20.0, print_object='no'):
                Grace()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('none')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=33.44, default_y=-146.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.37, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=101.31, default_y=-101.6):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=135.24, default_y=-111.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.17, default_y=-131.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Note(default_x=217.24, default_y=-86.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-98.51)
                Staff(2)
            with Note(default_x=262.46, default_y=-161.6):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=312.92, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=345.11, default_y=-111.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=379.04, default_y=-91.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=412.97, default_y=-96.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=446.91, default_y=-116.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(1680.0)
            with Note(default_x=296.03, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(960.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
            with Forward():
                Duration(240.0)
        with Measure(number='79', width=502.81):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=56.07)
                Staff(1)
            with Note(default_x=10.0, default_y=-20.0):
                Grace(slash='yes')
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=33.44, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
                Duration(480.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-23.99):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=103.49, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(7)
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
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=132.22, default_y=15.0):
                with Pitch():
                    Step('B')
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
                    with Articulations():
                        Staccato()
            with Note(default_x=168.12, default_y=5.0):
                with Pitch():
                    Step('G')
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=196.85, default_y=25.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    with Articulations():
                        Staccato()
            with Note(default_x=225.57, default_y=15.0):
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
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=261.47, default_y=-20.0):
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
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=290.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dimin.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-66.66)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-66.66)
                Staff(1)
            with Note(default_x=431.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.01)
                Staff(2)
            with Note(default_x=33.44, default_y=-156.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=68.47, default_y=-136.6):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.49, default_y=-121.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.17, default_y=-111.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.85, default_y=-91.6):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.52, default_y=-121.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-96.01)
                Staff(2)
            with Note(default_x=291.06, default_y=-131.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=326.09, default_y=-121.6):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=361.11, default_y=-106.6):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.14, default_y=-96.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
            with Note(default_x=431.16, default_y=-126.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=466.19, default_y=-96.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
        with Measure(number='80', width=783.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=66.67)
            with Note(default_x=120.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=450.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(960.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=671.45, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=120.74, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=175.81, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=230.88, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=285.95, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=341.03, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=396.1, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=451.17, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=506.24, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=561.31, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=616.38, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=671.45, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=726.53, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='81', width=765.71):
            with Direction(placement='below'):
                with DirectionType():
                    Words('smorz.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-72.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-72.0)
                Staff(1)
            with Note(default_x=10.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.98, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Note(default_x=372.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=410.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=447.69, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=485.36, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(120.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=23.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Staff(1)
                Sound(tempo=108.0)
            with Note(default_x=523.02, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note():
                Rest()
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=703.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=10.72, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=70.99, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.26, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.53, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=251.81, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.08, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.5)
                Staff(2)
            with Note(default_x=372.35, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=447.69, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=523.02, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=583.3, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=643.57, default_y=-75.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=703.84, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
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
        with Measure(number='82', width=577.27):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(79.67)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=50.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=120.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(960.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('92')
                Staff(1)
                Sound(tempo=92.0)
            with Note():
                Rest()
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_x=-10.67, relative_y=-23.99):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=345.35, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1440.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    with Articulations():
                        Accent()
            with Note(default_x=345.35, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(6)
                Duration(1440.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-83.51)
                Staff(2)
            with Note(default_x=120.74, default_y=-149.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.23, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=195.73, default_y=-104.67):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=233.22, default_y=-114.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=270.72, default_y=-94.67):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=308.21, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=-5.34)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-86.01)
                Staff(2)
            with Note(default_x=345.71, default_y=-149.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=383.2, default_y=-124.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=420.7, default_y=-119.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=458.19, default_y=-109.67):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=495.69, default_y=-99.67):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=533.18, default_y=-89.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Offset(-2400.0)
                Staff(1)
                Sound(tempo=96.0)
        with Measure(number='83', width=531.69):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('accelrando', default_y=-40.0, relative_y=-40.34, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('96')
                Staff(1)
                Sound(tempo=96.0)
            with Note(default_x=14.0, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
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
            with Note(default_x=14.0, default_y=40.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=38.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=54.21, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=54.21, default_y=30.0):
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
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=28.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('104')
                Staff(1)
                Sound(tempo=104.0)
            with Note(default_x=94.42, default_y=10.0):
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
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=94.42, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=18.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Staff(1)
                Sound(tempo=108.0)
            with Note(default_x=122.76, default_y=5.0):
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
                        Accent()
            with Note(default_x=134.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.3, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('112')
                Staff(1)
                Sound(tempo=112.0)
            with Note(default_x=174.83, default_y=-5.0):
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
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=174.83, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=6.28, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('116')
                Staff(1)
                Sound(tempo=116.0)
            with Note(default_x=215.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=215.04, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('dimin.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-96.01)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-96.01)
                Staff(1)
            with Note(default_x=255.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=255.25, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=283.59, default_y=-30.0):
                with Pitch():
                    Step('G')
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
                        Accent()
            with Note(default_x=295.45, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=335.66, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                        Accent()
            with Note(default_x=335.66, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=375.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=375.87, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('ritenuto', default_y=-40.4, relative_y=-17.66, font_style='italic', font_size='12')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('108')
                Staff(1)
                Sound(tempo=108.0)
            with Note(default_x=449.68, default_y=-119.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=449.68, default_y=-109.67):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Staff(1)
                Sound(tempo=100.0)
            with Note(default_x=489.88, default_y=-124.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Accent()
            with Note(default_x=501.75, default_y=-119.67):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=489.88, default_y=-99.67):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(240.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(2880.0)
            with Note(default_x=14.0, default_y=-144.67):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(960.0)
                Voice('5')
                Type('half')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(2)
        with Measure(number='84', width=307.22):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=4.0, relative_y=-18.65):
                        Ppp()
                Staff(1)
                Sound(dynamics=50.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('80')
                with DirectionType():
                    Words('\n', relative_y=20.0, font_weight='bold', font_size='12')
                    Words(None)
                Staff(1)
                Sound(tempo=80.0)
            with Note(default_x=17.44, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=17.44, default_y=-114.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=17.44, default_y=-104.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1440.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note(default_x=112.13, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.13, default_y=-114.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=112.13, default_y=-104.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('60')
                Staff(1)
                Sound(tempo=60.0)
            with Note(default_x=171.3, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=171.3, default_y=-114.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=171.3, default_y=-104.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('58')
                Staff(1)
                Sound(tempo=58.0)
            with Note(default_x=230.47, default_y=-114.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=230.47, default_y=-104.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(480.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(2880.0)
            with Forward():
                Duration(2400.0)
            with Note(default_x=245.47, default_y=-124.67):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('46')
                Staff(1)
                Sound(tempo=46.0)
            with Note(default_x=282.45, default_y=-129.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(240.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(2880.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-118.79, relative_x=-6.67)
                Staff(2)
            with Note(default_x=17.44, default_y=-184.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=17.44, default_y=-149.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1440.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=112.13, default_y=-184.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=112.13, default_y=-149.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.3, default_y=-184.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=171.3, default_y=-149.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.47, default_y=-184.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=230.47, default_y=-149.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(480.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='85', width=132.72):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('58')
                Staff(1)
                Sound(tempo=58.0)
            with Note(default_x=29.68, default_y=-139.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2880.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('natural')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=-95.0)
            with Note(default_x=29.68, default_y=-129.67):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2880.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=29.68, default_y=-114.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2880.0)
                Voice('1')
                Type('whole')
                Dot()
                Staff(2)
            with Note(default_x=29.68, default_y=-104.67):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2880.0)
                Voice('1')
                Type('whole')
                Dot()
                Accidental('natural')
                Staff(2)
            with Backup():
                Duration(2880.0)
            with Note(default_x=29.68, default_y=-184.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2880.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-40.0, relative_y=-35.0)
                    Arpeggiate(default_x=-19.73, default_y=-24.49, relative_x=-10.0)
            with Note(default_x=29.68, default_y=-149.67):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2880.0)
                Voice('5')
                Type('whole')
                Dot()
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-19.73, default_y=-24.49, relative_x=-10.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes', relative_x=32.01)
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')