with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Sonata in F minor')
    with Identification():
        Creator('Ludwig van Beethoven (1770-1827)', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-14')
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
        Source('http://musescore.com/user/6053266/scores/6115101')
    with Defaults():
        with Scaling():
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.54)
            PageWidth(1343.09)
            with PageMargins(type='even'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9387)
                RightMargin(63.9387)
                TopMargin(63.9387)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Sonata in F minor', default_x=671.547, default_y=1834.6, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Op. 2 No. 1, Movement I', default_x=671.547, default_y=1770.66, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Ludwig van Beethoven\n', default_x=1279.16, default_y=1734.6, justify='right', valign='bottom', font_size='8')
        CreditWords('(1770-1827)\n')
        CreditWords(None)
    with PartList():
        with ScorePart(id='P1'):
            PartName('Grand Piano')
            PartAbbreviation('Pno.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Grand Piano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=188.5):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(6.0)
                with Key():
                    Fifths(-4)
                with Time(symbol='cut'):
                    Beats('2')
                    BeatType('2')
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
                Sound(dynamics=54.44)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Allegro', default_x=-41.11, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=200.0)
            with Note(default_x=136.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='1', width=200.15):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=57.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=104.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=151.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
        with Measure(number='2', width=282.67):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=127.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=175.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=66.69, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.69, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.69, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.28, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.28, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.28, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.18, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.18, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=228.18, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=225.03):
            with Note(default_x=20.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=71.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=172.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=20.56, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=20.56, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=8.69, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=20.56, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='4', width=298.01):
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=114.75, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=137.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=182.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=71.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=71.0, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.13, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.0, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.01, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.01, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.15, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.01, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.21, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.21, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=227.35, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=239.21, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=350.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(106.36)
                with StaffLayout(number=2):
                    StaffDistance(82.58)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=88.89)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=110.38, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=128.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=204.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=220.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=264.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
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
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=171.43, default_y=-132.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.43, default_y=-122.58):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=171.43, default_y=-112.58):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=264.08, default_y=-132.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=264.08, default_y=-122.58):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=264.08, default_y=-112.58):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=306.69, default_y=-132.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=306.69, default_y=-122.58):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=306.69, default_y=-112.58):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='6', width=243.63):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=11.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=104.83, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=124.29, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=157.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
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
                    with Dynamics(default_x=5.33, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=72.48, default_y=-127.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.48, default_y=-117.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=72.48, default_y=-102.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=157.45, default_y=-127.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.45, default_y=-117.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.45, default_y=-102.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=199.74, default_y=-127.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=199.74, default_y=-117.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=199.74, default_y=-102.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='7', width=219.21):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=23.09, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=25.45)
            with Note(default_x=109.74, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=136.71, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=163.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=66.6, default_y=-122.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.6, default_y=-112.58):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=66.6, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=163.68, default_y=-117.58):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.68, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=163.68, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=211.44):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=20.11, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=31.08, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=42.04, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=53.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=92.78, default_y=-112.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=92.78, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=170.82, default_y=-162.58):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='9', width=169.2):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-147.58):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.4, default_y=-137.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=88.8, default_y=-127.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=128.2, default_y=-112.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='10', width=351.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(106.36)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=173.57, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=196.84, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.1, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=245.57, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=297.78, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='11', width=223.85):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=85.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
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
            with Note(default_x=145.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=183.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='12', width=198.85):
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=17.12, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=81.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.37, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=113.73, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=155.49, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-80.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='13', width=198.85):
            with Note(default_x=17.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=81.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
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
            with Note(default_x=113.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=155.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='14', width=221.21):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=84.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=100.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=142.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=181.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='15', width=275.84):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(106.36)
                with StaffLayout(number=2):
                    StaffDistance(85.73)
            with Note(default_x=114.54, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=154.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=234.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=111.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('2')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=39.51)
                Staff(2)
            with Note(default_x=114.18, default_y=-110.73):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=10.53, relative_y=30.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=40.0)
                Staff(2)
            with Note(default_x=194.03, default_y=-110.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
        with Measure(number='16', width=175.1):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=53.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=133.58, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=133.58, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Forward():
                Duration(18.0)
            with Note(default_x=133.58, default_y=-115.73):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='17', width=160.49):
            with Note(default_x=14.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=49.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=122.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=62.31)
                Staff(2)
            with Note(default_x=13.8, default_y=-100.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=28.56, relative_y=30.0):
                        Mp()
                Staff(2)
                Sound(dynamics=71.11)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=62.31)
                Staff(2)
            with Note(default_x=86.16, default_y=-100.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-110.73):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=86.16, default_y=-110.73):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=179.66):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.65, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=54.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(line_type='dotted', type='start', placement='below', number=2)
            with Note(default_x=54.87, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=95.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=95.93, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=137.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
                    Slur(type='stop', number=1)
            with Note(default_x=137.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=137.0, default_y=-140.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Forward():
                Duration(12.0)
            with Note(default_x=137.0, default_y=-150.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=168.82):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=51.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=51.79, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=128.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=128.86, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.44, default_y=-135.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=90.15, default_y=-135.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.44, default_y=-145.73):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=90.15, default_y=-145.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='20', width=234.46):
            with Note(default_x=13.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='stop', number=1)
            with Note(default_x=13.8, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=178.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-140.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.18, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.56, default_y=-140.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.95, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=123.33, default_y=-140.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=150.71, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=178.09, default_y=-140.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=205.48, default_y=-105.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='21', width=369.42):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(106.36)
                with StaffLayout(number=2):
                    StaffDistance(89.01)
            with Note(default_x=110.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=174.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=239.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=303.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.56, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.74, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=206.92, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=239.1, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=271.28, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=303.46, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=335.64, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='22', width=277.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=16.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=139.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=207.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.97, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.43, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=173.66, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.89, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.13, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.84, default_y=-114.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=139.43, default_y=-119.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='23', width=269.04):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=74.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=138.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=203.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.18, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.36, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.54, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=138.72, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.9, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.08, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.26, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='24', width=277.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=16.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=139.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=207.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.97, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.43, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=173.66, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=207.89, default_y=-144.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.13, default_y=-109.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.84, default_y=-114.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=139.43, default_y=-119.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='25', width=381.08):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(106.36)
                with StaffLayout(number=2):
                    StaffDistance(67.58)
            with Note(default_x=110.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=177.65, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=244.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=312.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-122.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=144.02, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=177.65, default_y=-122.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.29, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=244.93, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=278.57, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=312.21, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=345.85, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='26', width=282.29):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=47.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=80.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=113.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=180.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=247.33, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-97.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=47.16, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.52, default_y=-97.58):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=113.88, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=147.24, default_y=-112.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=180.61, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=213.97, default_y=-112.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=247.33, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='27', width=269.01):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=42.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=74.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=106.6, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=170.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=203.09, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=235.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-107.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.28, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=74.44, default_y=-107.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.6, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=138.76, default_y=-117.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=170.92, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.09, default_y=-107.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=235.25, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='28', width=261.99):
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=166.49, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=197.79, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=229.09, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-122.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.3, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.6, default_y=-112.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=103.89, default_y=-87.58):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=135.19, default_y=-117.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=166.49, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.79, default_y=-107.58):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=229.09, default_y=-92.58):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='29', width=318.68):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    TopSystemDistance(93.17)
                with StaffLayout(number=2):
                    StaffDistance(87.22)
            with Note(default_x=110.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=236.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=268.69, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=292.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.57, default_y=-107.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.77, default_y=-132.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.96, default_y=-107.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=211.83, default_y=-147.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=236.02, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=268.69, default_y=-137.22):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=292.88, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='30', width=206.26):
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=126.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=158.99, default_y=35.0):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=181.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-152.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.31, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=58.81, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.32, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=103.82, default_y=-147.22):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.33, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.99, default_y=-137.22):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.5, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='31', width=209.54):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=34.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=59.57, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=84.3, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=133.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.48, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.21, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-152.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=34.85, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.57, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=84.3, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.03, default_y=-167.22):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=133.76, default_y=-132.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.48, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.21, default_y=-132.22):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='32', width=214.1):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=35.42, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=60.71, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.01, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=136.61, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.9, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.2, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-162.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=35.42, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.71, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=86.01, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=111.31, default_y=-157.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.61, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.9, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.2, default_y=-122.22):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='33', width=245.79):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=38.63, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.15, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.66, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=130.13, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.65, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=187.16, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=215.67, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-152.22):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=66.79, default_y=-142.22):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=187.16, default_y=-127.22):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='34', width=264.01):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(129.82)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=110.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=128.79, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=184.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=202.43, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=220.83, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=239.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=146.84, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=220.83, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='35', width=174.63):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=28.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=55.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=74.4, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=93.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=112.13, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=131.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=149.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=55.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=131.0, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='36', width=173.63):
            with Note(default_x=20.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=75.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=93.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=112.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=130.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.87, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=20.0, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=56.82, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=93.64, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=130.46, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='37', width=213.03):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=38.5, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.21, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.91, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=112.62, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.32, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.02, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=186.73, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=62.85, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=162.02, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='38', width=167.43):
            with Note(default_x=13.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=32.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=50.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=87.44, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=105.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=124.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=142.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-160.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=50.26, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=124.26, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='39', width=201.63):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=83.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=106.92, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.19, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.47, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=176.75, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-155.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=60.0, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=153.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='40', width=340.38):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(119.12)
                with StaffLayout(number=2):
                    StaffDistance(73.45)
            with Note(default_x=114.18, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=142.25, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=170.33, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=198.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=226.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=254.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=282.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=310.71, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-133.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.33, default_y=-143.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=226.48, default_y=-153.45):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=282.63, default_y=-163.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='41', width=166.56):
            with Note(default_x=13.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('con espressione', default_y=-40.54, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=56.15, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=87.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=141.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-148.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=47.03, default_y=-113.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=121.02, default_y=-133.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=121.02, default_y=-123.45):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.02, default_y=-113.45):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.02, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='42', width=138.15):
            with Note(default_x=10.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=67.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=39.2, default_y=-128.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=39.2, default_y=-113.45):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.2, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=95.72, default_y=-128.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.72, default_y=-108.45):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.72, default_y=-98.45):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='43', width=182.57):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=45.01, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=70.79, default_y=-45.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=102.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=157.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=45.01, default_y=-113.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=45.01, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=136.5, default_y=-133.45):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=136.5, default_y=-123.45):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.5, default_y=-113.45):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=136.5, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='44', width=138.15):
            with Note(default_x=10.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=67.46, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=113.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=39.2, default_y=-128.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=39.2, default_y=-113.45):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=39.2, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=95.72, default_y=-128.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.72, default_y=-108.45):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=95.72, default_y=-98.45):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='45', width=228.56):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=52.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.82, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=113.26, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=201.27, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=52.05, default_y=-113.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=52.05, default_y=-103.45):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=175.58, default_y=-158.45):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=175.58, default_y=-148.45):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.58, default_y=-138.45):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=175.58, default_y=-128.45):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='46', width=264.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(119.12)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=112.61, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=183.08, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=240.05, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=148.02, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=148.02, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.02, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=218.14, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=218.14, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=218.14, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
        with Measure(number='47', width=107.07):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='above', number=2)
            with Note(default_x=32.31, default_y=-160.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-150.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=32.31, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='48', width=159.8):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(18.0)
            with Note(default_x=13.8, default_y=-165.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=13.8, default_y=-155.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-145.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=13.8, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='X1', implicit='yes', width=58.75):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=24.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(6.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='49', width=126.17):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=38.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=67.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=95.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
        with Measure(number='50', width=213.73):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=77.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=100.88, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=139.81, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=49.96, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=49.96, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=49.96, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.81, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.81, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=139.81, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.97, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.97, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=175.97, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='51', width=264.04):
            with Note(default_x=11.75, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.19, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.22, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=125.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.81, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=71.0, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.0, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.14, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=71.0, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.81, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.81, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=168.95, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.81, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.62, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.62, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=209.76, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.62, default_y=-85.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='52', width=229.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(119.12)
                with StaffLayout(number=2):
                    StaffDistance(72.58)
            with Note(default_x=110.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=139.83, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=169.28, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=198.74, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
        with Measure(number='53', width=262.72):
            with Note(default_x=11.75, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.19, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=101.6, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=124.86, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.93, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.2, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=70.65, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.65, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.79, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.65, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=180.2, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.2, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=168.33, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.2, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=220.66, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=220.66, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=208.79, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=220.66, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='54', width=293.96):
            with Note(default_x=11.75, default_y=-10.0):
                Grace(slash='yes')
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.19, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=116.25, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=139.51, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=194.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=78.95, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=78.95, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.09, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=78.95, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=194.84, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.84, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=182.98, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=194.84, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=243.6, default_y=-117.58):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=243.6, default_y=-107.58):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=231.74, default_y=-97.58):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=243.6, default_y=-92.58):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='55', width=207.85):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=17.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=159.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.36, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=64.91, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.47, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=112.02, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=135.58, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.14, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.69, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='56', width=200.05):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=57.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=104.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=151.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.56, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=57.11, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.67, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=104.22, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=127.78, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=151.34, default_y=-122.58):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.89, default_y=-87.58):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='57', width=268.7):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(119.12)
                with StaffLayout(number=2):
                    StaffDistance(94.01)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=121.58, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=163.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
                Sound(dynamics=54.44)
            with Note(default_x=188.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=227.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=121.58, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=147.26, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=188.58, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=211.84, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.89, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.93, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=121.22, default_y=-114.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=188.58, default_y=-119.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Forward():
                Duration(6.0)
        with Measure(number='58', width=154.85):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=44.31, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=78.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=112.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=27.15, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=44.31, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.46, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=78.62, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=95.77, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=112.93, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.08, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='59', width=163.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=16.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=57.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
                Sound(dynamics=54.44)
            with Note(default_x=83.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=122.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=41.87, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=83.19, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=106.46, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=122.5, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=138.55, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.84, default_y=-114.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=83.19, default_y=-119.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Forward():
                Duration(6.0)
        with Measure(number='60', width=185.25):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=48.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=90.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=137.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=29.14, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=48.28, default_y=-144.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.42, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=90.69, default_y=-114.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=113.95, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=137.22, default_y=-114.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.48, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='61', width=211.85):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=38.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=62.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=136.58, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-119.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.36, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.91, default_y=-119.01):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=87.47, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=112.02, default_y=-124.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.58, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.14, default_y=-124.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.69, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='62', width=210.41):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=31.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.48, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=137.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=164.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=185.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-129.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=31.24, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=52.36, default_y=-129.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=73.48, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=104.16, default_y=-134.01):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.85, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=164.52, default_y=-134.01):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.64, default_y=-109.01):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='63', width=288.0):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(99.01)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Fp()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=119.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=242.66, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=119.18, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.76, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.34, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.92, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=201.5, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=222.08, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.66, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=263.24, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='64', width=178.82):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=51.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=92.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=133.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.58, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=51.16, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.74, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=92.32, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=112.9, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.48, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.06, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='65', width=185.7):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
                Sound(dynamics=54.44)
            with Note(default_x=94.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=139.58, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.16, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=48.33, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=94.96, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=118.23, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=139.58, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.94, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-114.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=94.96, default_y=-119.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='66', width=178.82):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=51.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=92.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=133.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=30.58, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=51.16, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=71.74, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=92.32, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=112.9, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=133.48, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=154.06, default_y=-109.01):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='67', width=170.99):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=63.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
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
                Sound(dynamics=54.44)
            with Note(default_x=89.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=119.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.16, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=44.68, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=89.03, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=119.55, default_y=-139.01):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-114.01):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=89.03, default_y=-119.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='68', width=192.02):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.67, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=58.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=101.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=145.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=167.26, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-144.01):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.43, default_y=-149.01):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.96, default_y=-159.01):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=145.49, default_y=-169.01):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='69', width=326.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(123.22)
                with StaffLayout(number=2):
                    StaffDistance(71.45)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=164.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=218.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=111.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=138.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.58, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=218.34, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=245.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=271.85, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=298.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(2)
            with Note(default_x=111.32, default_y=-146.45):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=191.58, default_y=-151.45):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=218.34, default_y=-136.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=271.85, default_y=-116.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
        with Measure(number='70', width=196.83):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.15, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=56.3, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=79.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=102.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=125.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=148.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-121.45):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=56.3, default_y=-126.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=102.61, default_y=-136.45):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.91, default_y=-146.45):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='71', width=234.24):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=69.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=126.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.38, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=126.57, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=153.09, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=179.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=206.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-41.43, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-79.08)
                Staff(2)
            with Note(default_x=16.2, default_y=-151.45):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(2)
                Duration(9.0)
                Voice('5')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=95.9, default_y=-156.45):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=126.57, default_y=-141.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=179.6, default_y=-121.45):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
        with Measure(number='72', width=215.07):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.43, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=60.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=86.3, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=111.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.17, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=162.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=188.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-126.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=60.87, default_y=-131.45):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=111.74, default_y=-141.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=162.6, default_y=-151.45):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='73', width=221.27):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=117.57, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.63, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=67.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=117.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=143.37, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-61.28, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=194.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.2, default_y=-156.45):
                with Pitch():
                    Step('F')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=66.71, default_y=-161.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=168.8, default_y=-126.45):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='74', width=299.28):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(123.22)
                with StaffLayout(number=2):
                    StaffDistance(75.57)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=205.62, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.44, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=160.29, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=183.13, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=205.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-68.78, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=228.82, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=251.67, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.51, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-130.57):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=159.93, default_y=-140.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=251.67, default_y=-175.57):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='75', width=207.15):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=109.32, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=61.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=85.71, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=109.68, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.65, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=157.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-66.28, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=181.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-175.57):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=61.38, default_y=-170.57):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=157.62, default_y=-135.57):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='76', width=203.35):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=105.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=33.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=57.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=81.91, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=105.88, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-71.28, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=129.85, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=153.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=177.78, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-135.57):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=57.58, default_y=-145.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=153.82, default_y=-180.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='77', width=245.51):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=128.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.56, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=71.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.09, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=128.85, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=157.62, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=186.38, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-76.28, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=215.14, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-180.57):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=70.97, default_y=-175.57):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=106.67)
            with Note(default_x=186.38, default_y=-140.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='78', width=239.07):
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=125.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.76, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.72, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=97.68, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.64, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-78.78, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=153.6, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=181.56, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.51, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-140.57):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.36, default_y=-150.57):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=181.56, default_y=-185.57):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='79', width=324.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(-0.0)
                    SystemDistance(123.22)
                with StaffLayout(number=2):
                    StaffDistance(69.4)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=216.82, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=111.32, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.78, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=164.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=190.71, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=217.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-76.28, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=243.64, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=270.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=296.57, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=163.89, default_y=-174.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=270.11, default_y=-139.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='80', width=254.68):
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.89, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=73.77, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=73.77, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=103.66, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.54, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=133.54, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=133.54, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=163.43, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.31, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.31, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=193.31, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=223.2, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=73.41, default_y=-174.4):
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(12.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=193.31, default_y=-139.4):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='81', width=212.4):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.88, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=17.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=17.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=163.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-169.4):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.56, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.23, default_y=-124.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.99, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.75, default_y=-124.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=139.52, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.28, default_y=-124.4):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.04, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='82', width=191.4):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=144.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-119.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=32.38, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=54.75, default_y=-119.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=77.13, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=99.51, default_y=-119.4):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=121.88, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=144.26, default_y=-109.4):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.64, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='83', width=211.24):
            with Note(default_x=14.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=161.99, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.0, default_y=-114.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.83, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=61.65, default_y=-114.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=85.48, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.3, default_y=-114.4):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=133.13, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=161.99, default_y=-104.4):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=185.82, default_y=-134.4):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='84', width=325.34):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(123.22)
                with StaffLayout(number=2):
                    StaffDistance(70.98)
            with Note(default_x=110.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=214.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=214.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-110.98):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=136.42, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=162.46, default_y=-100.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.49, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=215.16, default_y=-105.98):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=241.2, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=271.66, default_y=-95.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=297.7, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='85', width=220.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=17.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
                    with Articulations():
                        Staccato()
            with Note(default_x=17.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=169.1, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=188.77, default_y=-20.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(4)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=199.74, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-100.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.73, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=69.39, default_y=-125.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=94.32, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=119.25, default_y=-125.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=144.17, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=169.1, default_y=-115.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=194.03, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='86', width=199.55):
            with Note(default_x=10.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=56.75, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=150.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=167.77, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=178.74, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=33.38, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=56.75, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=80.13, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=103.5, default_y=-120.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=126.88, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.26, default_y=-110.98):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=173.63, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='87', width=223.95):
            with Note(default_x=14.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=65.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=171.07, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Ornaments():
                        TrillMark()
            with Note(default_x=192.17, default_y=15.0):
                Grace()
                with Pitch():
                    Step('B')
                    Octave(5)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=203.14, default_y=20.0):
                Grace()
                with Pitch():
                    Step('C')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.0, default_y=-115.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.64, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=65.28, default_y=-115.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.92, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=116.57, default_y=-115.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=142.21, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=171.07, default_y=-105.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.71, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='88', width=224.96):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=62.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=171.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.29, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-110.98):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.04, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=62.08, default_y=-100.98):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=88.12, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=114.78, default_y=-105.98):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.82, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=171.29, default_y=-95.98):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=197.32, default_y=-135.98):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='89', width=304.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(123.22)
                with StaffLayout(number=2):
                    StaffDistance(84.2)
            with Note(default_x=122.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=122.98, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=165.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=165.74, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=258.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=258.75, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=122.98, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=144.36, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=165.74, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=187.12, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=215.99, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=237.37, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=258.75, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=280.13, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='90', width=210.84):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=59.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.86, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('decresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=163.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=163.04, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-124.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.83, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.86, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=82.88, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.55, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.58, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.04, default_y=-109.2):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.07, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='91', width=199.72):
            with Note(default_x=17.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=17.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=60.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=60.56, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=153.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=153.57, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.18, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=60.56, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=81.94, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=110.81, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.19, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.57, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=174.95, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='92', width=210.84):
            with Note(default_x=13.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=59.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=59.86, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=163.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=163.04, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-124.2):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=36.83, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=59.86, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=82.88, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=109.55, default_y=-119.2):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.58, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=163.04, default_y=-109.2):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=186.07, default_y=-149.2):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='93', width=136.04):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=17.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=17.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(12.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=46.96, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=76.12, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.28, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='94', width=132.04):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=42.96, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=72.12, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.28, default_y=-114.2):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
        with Measure(number='95', width=394.64):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=225.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=254.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
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
            with Note(default_x=293.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=125.38, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=137.25, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=175.27, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.14, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=281.4, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=293.27, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=331.29, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=343.15, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='96', width=254.23):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=93.04, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=116.3, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.57, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=162.84, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.7, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=58.7, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=162.84, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=162.84, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=207.73, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=207.73, default_y=-90.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='97', width=280.7):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=108.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=135.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.76, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=180.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.05, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=70.92, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.99, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=218.18, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=230.05, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='98', width=264.79):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=93.86, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=117.13, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=172.46, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.17, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=59.17, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=172.46, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=172.46, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.83, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=217.83, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='99', width=367.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(126.85)
                with StaffLayout(number=2):
                    StaffDistance(84.31)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=205.89, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=232.56, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
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
            with Note(default_x=271.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.38, default_y=-124.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=122.24, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=157.78, default_y=-124.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=169.64, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=259.62, default_y=-124.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=271.49, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=307.02, default_y=-124.31):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=318.89, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='100', width=268.81):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=97.87, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=121.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.2, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=176.47, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-129.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.8, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=17.8, default_y=-104.31):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=63.17, default_y=-129.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=63.17, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=63.17, default_y=-104.31):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.47, default_y=-129.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.47, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=176.47, default_y=-104.31):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.84, default_y=-129.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.84, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=221.84, default_y=-104.31):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='101', width=153.38):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-43.54, relative_y=-40.0):
                        F()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.29, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=82.79, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=117.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-134.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-124.31):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-114.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='102', width=230.97):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=87.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=103.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=146.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=55.33, default_y=-134.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.33, default_y=-124.31):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.33, default_y=-114.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.31, default_y=-134.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.31, default_y=-124.31):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=146.31, default_y=-114.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.84, default_y=-134.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.84, default_y=-124.31):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=187.84, default_y=-114.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='103', width=173.33):
            with Note(default_x=20.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=58.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=96.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=133.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=20.56, default_y=-139.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=20.56, default_y=-129.31):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=8.69, default_y=-119.31):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=20.56, default_y=-114.31):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='104', width=394.12):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(126.85)
                with StaffLayout(number=2):
                    StaffDistance(85.98)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=114.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        Accent()
            with Note(default_x=213.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=235.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=279.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=170.51, default_y=-140.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=170.51, default_y=-130.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=158.65, default_y=-120.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=170.51, default_y=-115.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=279.85, default_y=-140.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=279.85, default_y=-130.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=267.98, default_y=-120.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=279.85, default_y=-115.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.19, default_y=-140.98):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.19, default_y=-130.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=324.32, default_y=-120.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=336.19, default_y=-115.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='105', width=277.64):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=11.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=30.19, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=115.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=164.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Direction(placement='below'):
                with DirectionType():
                    Dynamics(default_y=-49.4)
                Staff(2)
            with Note(default_x=29.83, default_y=-135.98):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=29.83, default_y=-125.98):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=29.83, default_y=-115.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='106', width=260.87):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=4.75, default_y=-15.0):
                Grace(slash='yes')
                with Pitch():
                    Step('C')
                    Octave(5)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=23.19, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=106.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=149.81, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=22.83, default_y=-130.98):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=22.83, default_y=-120.98):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=22.83, default_y=-105.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(12.0)
                Voice('5')
                Type('half')
                Staff(2)
        with Measure(number='107', width=261.74):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=25.45)
            with Note(default_x=23.09, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=25.45)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=25.45)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.81, default_y=25.45)
            with Note(default_x=128.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=161.52, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=194.39, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=23.45, default_y=-125.98):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=23.45, default_y=-115.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=23.45, default_y=-100.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=128.64, default_y=-120.98):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=128.64, default_y=-110.98):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=128.64, default_y=-95.98):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='108', width=315.68):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(126.85)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=116.54, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.5, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.47, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=191.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=150.19, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=150.19, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_y=30.0):
                        P()
                Staff(2)
                Sound(dynamics=54.44)
            with Note(default_x=273.11, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='109', width=182.84):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=51.56, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=93.12, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=134.68, default_y=-80.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='110', width=221.6):
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=63.18, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
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
            with Note(default_x=81.51, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.18, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=126.5, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=173.25, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
        with Measure(number='111', width=233.94):
            with Note(default_x=17.53, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=70.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
            with Note(default_x=101.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=138.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=185.38, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=14.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=32.71, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
        with Measure(number='112', width=240.3):
            with Note(default_x=14.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('2')
                Type('eighth')
                Staff(1)
            with Note(default_x=92.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=109.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=136.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=153.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=195.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=14.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=14.21, default_y=-135.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Accidental('flat')
                Staff(2)
        with Measure(number='113', width=390.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(126.85)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=120.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=191.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=215.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=241.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=266.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=327.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=117.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=117.61, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=117.61, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
        with Measure(number='114', width=267.45):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(9.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=78.84, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=101.42, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=150.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=208.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=10.0, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='115', width=290.69):
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=114.45, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no', show_number='none')
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=161.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=182.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=235.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('2')
                Type('whole')
                Accidental('natural')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(24.0)
            with Note(default_x=20.28, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(18.0)
                Voice('5')
                Type('half')
                Dot()
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=235.94, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.32, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='116', width=245.33):
            with Note(default_x=23.32, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Note(default_x=78.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=133.53, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=188.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=20.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('2')
                Type('whole')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Backup():
                Duration(24.0)
            with Note(default_x=23.32, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=78.42, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=133.53, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=188.63, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=20.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Tie(type='stop')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
        with Measure(number='117', width=277.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(126.85)
                with StaffLayout(number=2):
                    StaffDistance(87.15)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=120.93, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=159.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=198.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=236.82, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=120.93, default_y=-167.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=159.56, default_y=-157.15):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=198.19, default_y=-162.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=236.82, default_y=-167.15):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=117.61, default_y=-177.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='118', width=230.42):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=14.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=66.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=118.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=171.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.16, default_y=-162.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=66.58, default_y=-147.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=118.99, default_y=-152.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=171.4, default_y=-162.15):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-177.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.63, default_y=-172.15):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('6')
                Type('half')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='119', width=232.12):
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=14.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=14.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=176.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=14.0, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.07, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=68.13, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.2, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=122.26, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=149.33, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=176.39, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=203.46, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='120', width=228.12):
            with Note(default_x=10.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=118.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=172.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=37.07, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=64.13, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=91.2, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=118.26, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=145.33, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=172.39, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=199.46, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='121', width=226.64):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-45.64, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-81.13)
                Staff(1)
            with Note(default_x=10.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=83.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=112.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=168.55, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.36, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=55.56, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.05, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.3, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=168.55, default_y=-152.15):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=196.8, default_y=-117.15):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-122.15):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=112.05, default_y=-127.15):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='122', width=300.96):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    TopSystemDistance(83.71)
                with StaffLayout(number=2):
                    StaffDistance(81.51)
            with Note(default_x=114.18, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=160.47, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=206.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=253.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=137.32, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=160.47, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=183.61, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=206.76, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=229.91, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.05, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=276.2, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='123', width=183.77):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=10.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=68.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
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
                Sound(dynamics=54.44)
            with Note(default_x=91.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccato()
            with Note(default_x=136.49, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.36, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=46.4, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=91.44, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=113.96, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=136.49, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=159.01, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('6')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Note(default_x=91.44, default_y=-121.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Forward():
                Duration(6.0)
        with Measure(number='124', width=218.82):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=64.66, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=115.51, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=166.37, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.23, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=64.66, default_y=-146.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.08, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=115.51, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=140.94, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=166.37, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.8, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='125', width=248.78):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=39.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.15, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=98.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=158.64, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=188.16, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=217.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-121.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=39.63, default_y=-96.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=69.15, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=98.66, default_y=-96.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=128.18, default_y=-126.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=158.64, default_y=-101.51):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=188.16, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=217.67, default_y=-101.51):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='126', width=242.02):
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=38.91, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.69, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=96.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=154.06, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=182.85, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=211.64, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-131.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.91, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.69, default_y=-121.51):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=96.48, default_y=-111.51):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=125.27, default_y=-141.51):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=154.06, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.85, default_y=-131.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.64, default_y=-116.51):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='127', width=382.92):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(122.03)
                with StaffLayout(number=2):
                    StaffDistance(80.68)
            with Note(default_x=114.18, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=281.14, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=314.53, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=347.92, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-145.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.57, default_y=-110.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=180.96, default_y=-135.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=214.35, default_y=-110.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=247.75, default_y=-140.68):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=281.14, default_y=-115.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=314.53, default_y=-130.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=347.92, default_y=-115.68):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='128', width=294.1):
            with Note(default_x=13.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=187.99, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=222.82, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=257.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-145.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=48.64, default_y=-110.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=83.47, default_y=-135.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=118.31, default_y=-110.68):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=153.15, default_y=-150.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=187.99, default_y=-125.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=222.82, default_y=-140.68):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=257.66, default_y=-125.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='129', width=240.86):
            with Note(default_x=10.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=153.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=181.94, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        Mordent()
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=210.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-155.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=38.66, default_y=-130.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=67.31, default_y=-145.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=95.97, default_y=-130.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=124.63, default_y=-150.68):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=153.29, default_y=-125.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=181.94, default_y=-140.68):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=210.6, default_y=-125.68):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='130', width=276.5):
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=43.22, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=76.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=109.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=175.61, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=208.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=241.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-155.68):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.22, default_y=-130.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=76.31, default_y=-145.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=109.41, default_y=-130.68):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=142.51, default_y=-170.68):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=175.61, default_y=-135.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.7, default_y=-145.68):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=241.8, default_y=-135.68):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='131', width=304.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(122.03)
                with StaffLayout(number=2):
                    StaffDistance(85.7)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=134.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.68, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=182.77, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=230.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=255.04, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=279.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.5, default_y=-170.7):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=134.59, default_y=-135.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=158.68, default_y=-150.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.77, default_y=-135.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=206.86, default_y=-165.7):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=230.95, default_y=-130.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=255.04, default_y=-150.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=279.13, default_y=-130.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='132', width=254.14):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=39.03, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.94, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=102.42, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=160.24, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=189.15, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=223.62, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.12, default_y=-160.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=67.58, default_y=-150.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=189.15, default_y=-135.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='133', width=172.4):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=29.66, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=49.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=88.65, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=108.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=127.98, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=147.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-155.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=48.96, default_y=-145.7):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=127.98, default_y=-130.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='134', width=237.2):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=37.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=65.3, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.63)
                Staff(1)
            with Note(default_x=92.94, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=125.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=152.66, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=180.31, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=207.96, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
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
                Duration(24.0)
            with Note(default_x=10.0, default_y=-150.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=64.94, default_y=-135.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=180.31, default_y=-125.7):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='135', width=225.8):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-46.4, relative_y=-40.0):
                        Pp()
                Staff(1)
                Sound(dynamics=36.67)
            with Note(default_x=17.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.6, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=95.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=121.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=172.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=198.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.8, default_y=-120.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=69.4, default_y=-130.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=121.0, default_y=-140.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=172.6, default_y=-155.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='136', width=392.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(122.03)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=5.06, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=145.51, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=180.52, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=215.53, default_y=30.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=250.54, default_y=25.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=285.55, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=320.56, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=355.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=110.5, default_y=-140.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=180.16, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=320.56, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='137', width=223.51):
            with Note(default_x=10.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=36.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=62.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=89.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=115.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=142.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=168.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=195.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=10.0, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=62.62, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=168.94, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='138', width=279.19):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=76.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-83.63)
                Staff(1)
            with Note(default_x=110.35, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=143.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.25, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=210.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=244.14, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
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
                Duration(24.0)
            with Note(default_x=10.0, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(2)
                Sound(dynamics=124.44)
            with Note(default_x=76.54, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('5')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=210.7, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='139', width=299.48):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Staff(1)
                Sound(dynamics=54.44)
            with Note(default_x=17.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=52.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=87.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=122.83, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=192.85, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.86, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=262.87, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=87.82, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=157.84, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=227.86, default_y=-165.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
        with Measure(number='140', width=272.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(122.03)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=114.18, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('con espressione', default_y=-40.0, relative_y=-35.0, font_style='italic', font_size='11')
                Staff(1)
            with Note(default_x=182.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=237.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=114.18, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=148.32, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=216.61, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=216.61, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=216.61, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='141', width=150.0):
            with Note(default_x=10.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=74.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=42.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.47, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.47, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.47, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.53, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.53, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=105.53, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='142', width=182.2):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=106.67)
            with Note(default_x=10.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Staff(1)
                Sound(dynamics=71.11)
            with Note(default_x=48.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=86.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=147.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=48.7, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=48.7, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=124.22, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=124.22, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=112.36, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=124.22, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='143', width=150.0):
            with Note(default_x=10.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Note(default_x=74.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=125.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=42.47, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=42.47, default_y=-115.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.47, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=42.47, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.53, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.53, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=105.53, default_y=-100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
        with Measure(number='144', width=228.6):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note(default_x=57.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.33, default_y=-20.0):
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
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=103.77, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=197.99, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=57.35, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=57.35, default_y=-105.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('G')
                    Line(2)
            with Note(default_x=168.98, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=168.98, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=168.98, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=180.85, default_y=-125.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
        with Measure(number='145', width=211.24):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
                Staff(1)
            with Note(default_x=10.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=88.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(9.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=185.32, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=49.86, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=49.86, default_y=-140.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=49.86, default_y=-130.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=49.86, default_y=-120.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Attributes():
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note(default_x=149.13, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=160.99, default_y=-95.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=160.99, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='146', width=221.75):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(20.85)
                        RightMargin(0.0)
                    SystemDistance(122.03)
                with StaffLayout(number=2):
                    StaffDistance(84.95)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=125.38, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='above', number=1)
            with Note(default_x=125.38, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Accidental('flat')
                Staff(1)
            with Note(default_x=125.38, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=125.38, default_y=-124.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Accidental('natural')
                Staff(2)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='below', number=2)
            with Note(default_x=125.38, default_y=-114.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=125.38, default_y=-99.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='147', width=179.18):
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=153.5, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.5, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=153.5, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-119.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=13.8, default_y=-109.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-99.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=153.5, default_y=-119.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=153.5, default_y=-109.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=153.5, default_y=-99.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='148', width=114.96):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='above', number=1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Note(default_x=13.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(24.0)
                Voice('1')
                Type('whole')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-129.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
                with Notations():
                    Slur(line_type='dotted', type='start', placement='below', number=2)
            with Note(default_x=13.8, default_y=-119.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Note(default_x=13.8, default_y=-104.95):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(24.0)
                Voice('5')
                Type('whole')
                Staff(2)
        with Measure(number='149', width=160.38):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=122.54, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.54, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=122.54, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-124.95):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=13.8, default_y=-114.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=13.8, default_y=-104.95):
                Chord()
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=122.54, default_y=-134.95):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=122.54, default_y=-109.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='150', width=190.7):
            with Note(default_x=13.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
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
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-43.35, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=57.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=57.62, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=57.62, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=101.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.45, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=101.45, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-47.1, relative_y=-40.0):
                        Sf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=145.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.27, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=145.27, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-129.95):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=13.8, default_y=-109.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=57.62, default_y=-139.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=57.62, default_y=-114.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=101.45, default_y=-134.95):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=101.45, default_y=-114.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=145.27, default_y=-144.95):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=145.27, default_y=-109.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='151', width=190.25):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-47.1, relative_y=-40.0):
                        Ff()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.87, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=21.87, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=105.26, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.26, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=105.26, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=117.12, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=105.26, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note(default_x=21.87, default_y=-154.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=21.87, default_y=-144.95):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-129.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=21.87, default_y=-119.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=105.26, default_y=-149.95):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=105.26, default_y=-139.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=105.26, default_y=-129.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=105.26, default_y=-114.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
        with Measure(number='152', width=137.15):
            with Note(default_x=10.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=10.0, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(18.0)
            with Note(default_x=10.0, default_y=-169.95):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccato()
            with Note(default_x=10.0, default_y=-159.95):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-149.95):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=10.0, default_y=-134.95):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Staff(2)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')