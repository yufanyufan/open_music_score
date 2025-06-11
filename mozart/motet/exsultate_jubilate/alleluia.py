with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Alleluia')
    with Identification():
        Creator(' W A Mozart', type='composer')
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
        CreditWords('Alleluia', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords(' W A Mozart', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Flute')
            PartAbbreviation('Fl.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(74)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('B♭ Clarinet')
            PartAbbreviation('B♭ Cl.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('B♭ Clarinet')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(72)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('B♭ Clarinet')
            PartAbbreviation('B♭ Cl.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('B♭ Clarinet')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(72)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=177.45):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(116.8)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(40.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=152.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=106.4):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=63.96):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=65.96):
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=39.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=89.53):
            with Note(default_x=16.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=106.4):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=98.42):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=73.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=64.99):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=81.19):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=56.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='10', width=106.4):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=152.65):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(91.09)
            with Note(default_x=87.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=66.17):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=145.7):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.32, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=108.88):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=64.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=91.22):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.15, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=48.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.46, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='16', width=57.79):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=218.82):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=30.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.44, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=93.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=112.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=130.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.05, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='18', width=74.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=44.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='19', width=95.77):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=51.53, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='20', width=201.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(91.09)
            with Note(default_x=87.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=238.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=33.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=123.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=144.38, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.33, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('16th')
                with TimeModification():
                    ActualNotes(5)
                    NormalNotes(4)
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Tuplet(type='stop')
        with Measure(number='22', width=93.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=54.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='23', width=115.04):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=70.81, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=90.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='24', width=82.3):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=165.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=15.8, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=55.68, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=78.95, default_y=35.0):
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=129.01, default_y=30.0):
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='26', width=115.92):
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=40.43, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=89.69, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
        with Measure(number='27', width=228.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(91.09)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-75.0)
            with Note(default_x=91.01, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(30.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=132.73, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=156.0, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(5.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=199.18, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='28', width=98.83):
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=35.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=74.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='29', width=141.51):
            with Note(default_x=16.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=65.17, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.43, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=89.96):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=39.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=58.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='31', width=90.26):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=119.73):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=95.76):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='34', width=146.73):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=38.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=71.98, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=88.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.3, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='35', width=251.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=87.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.31, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=203.05, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.32, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='36', width=204.76):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.06, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='37', width=179.68):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=54.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.63, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.18, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.65, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.91, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='38', width=204.76):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.64, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.06, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=109.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='39', width=170.81):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=62.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=80.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.51, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=122.78, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.04, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='40', width=154.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=91.01, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=129.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='41', width=93.03):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='42', width=108.69):
            with Note(default_x=12.36, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='43', width=58.88):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=92.31):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='45', width=92.31):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='46', width=97.54):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=54.26, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=63.08):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.31, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=66.68):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='49', width=93.03):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='50', width=91.46):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='51', width=177.06):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=87.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='52', width=101.86):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='53', width=101.86):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='54', width=107.09):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=82.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=72.63):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='56', width=76.23):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='57', width=102.58):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='58', width=101.0):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='59', width=170.79):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='60', width=242.71):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(-0.0)
                    SystemDistance(124.43)
            with Note(default_x=87.21, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='61', width=150.27):
            with Note(default_x=12.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='62', width=111.74):
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='63', width=98.93):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='64', width=98.93):
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.57, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='65', width=76.27):
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=76.21):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.3, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='67', width=76.27):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=79.76):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.08, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
        with Measure(number='69', width=167.13):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=87.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='70', width=63.18):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='71', width=79.74):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='72', width=63.54):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='73', width=73.95):
            with Note(default_x=15.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='74', width=79.18):
            with Note(default_x=20.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
        with Measure(number='75', width=57.86):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='76', width=57.86):
            with Note(default_x=16.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='77', width=61.79):
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=66.62):
            with Note(default_x=15.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=96.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='80', width=143.26):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=118.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='81', width=225.36):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(122.62)
            with Note(default_x=96.01, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.75, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=166.98, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='82', width=143.35):
            with Note(default_x=14.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=49.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='83', width=112.12):
            with Note(default_x=16.87, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='84', width=167.49):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=76.72, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=99.99, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='85', width=145.53):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=48.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=85.89, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='86', width=217.24):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.78, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.76, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.74, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=115.72, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=140.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.68, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.66, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='87', width=252.58):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(122.62)
            with Note(default_x=87.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.32, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.88, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=165.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=184.99, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.55, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.81, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='88', width=206.25):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.41, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.01, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.62, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='89', width=177.37):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.11, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.61, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='90', width=206.25):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.41, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.01, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.62, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.23, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.83, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.44, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='91', width=168.63):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.1, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
            with Note(default_x=88.98, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
        with Measure(number='92', width=199.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(122.62)
            with Note(default_x=87.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='93', width=171.43):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.49, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='94', width=127.58):
            with Note(default_x=15.44, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='95', width=171.43):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=15.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.49, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=71.88, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=90.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=109.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='96', width=127.94):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='97', width=110.86):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=39.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=85.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='98', width=102.5):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.74, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='99', width=171.11):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=87.21, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=106.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.34, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='100', width=99.7):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=35.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='101', width=61.44):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=62.47):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='103', width=80.84):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='104', width=100.08):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='105', width=73.6):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='106', width=74.65):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='107', width=78.67):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='108', width=100.08):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='109', width=108.44):
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='110', width=136.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note():
                Rest(measure='yes')
                Duration(80.0)
                Voice('1')
        with Measure(number='111', width=77.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=52.95, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='112', width=94.95):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='113', width=60.48):
            with Note(default_x=12.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.44, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=65.71):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=40.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='115', width=78.44):
            with Note(default_x=12.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.67, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='116', width=94.95):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='117', width=94.95):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='118', width=94.95):
            with Note(default_x=12.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='119', width=109.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=74.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='120', width=102.93):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.59, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='121', width=181.23):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=87.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=146.86, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='122', width=99.64):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='123', width=57.07):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='124', width=57.07):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='125', width=57.03):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='126', width=83.06):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=41.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='127', width=109.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=75.45, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='128', width=103.44):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='129', width=106.03):
            with Note(default_x=12.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=71.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='130', width=99.64):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='131', width=57.07):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='132', width=130.3):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    SystemDistance(124.43)
            with Note(default_x=87.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='133', width=67.25):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='134', width=67.25):
            with Note(default_x=15.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='135', width=67.25):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='136', width=67.25):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='137', width=67.25):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='138', width=152.78):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=58.22, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.49, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.75, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.02, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='139', width=127.7):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=69.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='140', width=73.14):
            with Note(default_x=12.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='141', width=190.91):
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=101.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='142', width=458.91):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(66.4)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=87.21, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=272.26, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='143', width=271.57):
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=142.89, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='144', width=280.61):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=177.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(40.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-1)
                    Chromatic(-2.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.26, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=152.69, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='2', width=106.4):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=63.96):
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.18, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='4', width=65.96):
            with Note(default_x=14.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.18, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='5', width=89.53):
            with Note(default_x=16.16, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.3, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.76, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=106.4):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=98.42):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.55, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.1, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.66, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=64.99):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=81.19):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=56.42, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='10', width=106.4):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=37.75, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=59.69, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.64, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=152.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-85.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.68, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
        with Measure(number='12', width=66.17):
            with Note(default_x=17.23, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=40.9, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='13', width=145.7):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=43.06, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.32, default_y=-85.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.59, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=116.84, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=108.88):
            with Note(default_x=15.8, default_y=-95.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=44.07, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=64.09, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=84.12, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=91.22):
            with Note(default_x=12.0, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.15, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=48.31, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.46, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=57.79):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=218.82):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.22, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=74.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=44.86, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=95.77):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.04, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='20', width=201.36):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='21', width=238.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=123.24, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=93.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=54.5, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=115.04):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.2, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='24', width=82.3):
            with Note(default_x=17.23, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=165.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.98, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.98)
            with Note(default_x=15.44, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='26', width=115.92):
            with Note(default_x=15.44, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='27', width=228.3):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-50.98, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-85.98)
            with Note(default_x=90.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='28', width=98.83):
            with Note(default_x=15.44, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='29', width=141.51):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='30', width=89.96):
            with Note(default_x=15.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='31', width=90.26):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.83, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='32', width=119.73):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='33', width=95.76):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.14, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.57, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.99, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='34', width=146.73):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=38.66, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=71.98, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.3, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=251.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=164.31, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='36', width=204.76):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.48, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=179.68):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.91, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='38', width=204.76):
            with Note(default_x=15.8, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.48, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=170.81):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='40', width=154.09):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=113.65, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='41', width=93.03):
            with Note(default_x=12.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='42', width=108.69):
            with Note(default_x=12.72, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.37, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.27, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=83.92, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='43', width=58.88):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=92.31):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=30.52, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.55, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=92.31):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.52, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.55, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='46', width=97.54):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=54.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='47', width=63.08):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=38.31, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='48', width=66.68):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=41.92, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='49', width=93.03):
            with Note(default_x=12.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.24, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=49.75, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.27, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='50', width=91.46):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=36.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=66.69, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='51', width=177.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='52', width=101.86):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.7, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=55.4, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.09, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='53', width=101.86):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.7, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.4, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.09, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='54', width=107.09):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=60.63, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='55', width=72.63):
            with Note(default_x=17.23, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=44.13, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='56', width=76.23):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=51.46, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='57', width=102.58):
            with Note(default_x=12.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.42, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.12, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.81, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='58', width=101.0):
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=46.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.24, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='59', width=170.79):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='60', width=242.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='61', width=150.27):
            with Note(default_x=12.0, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='62', width=111.74):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='63', width=98.93):
            with Note(default_x=12.36, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.57, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.17, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=98.93):
            with Note(default_x=12.36, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.57, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=74.17, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='65', width=76.27):
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='66', width=76.21):
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.3, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=76.27):
            with Note(default_x=15.8, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.23, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='68', width=79.76):
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.08, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='69', width=167.13):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.57, default_y=-170.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=121.29, default_y=-160.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=142.36, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='70', width=63.18):
            with Note(default_x=12.36, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='71', width=79.74):
            with Note(default_x=12.72, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=38.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=54.98, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='72', width=63.54):
            with Note(default_x=12.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='73', width=73.95):
            with Note(default_x=15.8, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.07, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='74', width=79.18):
            with Note(default_x=21.03, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=49.31, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='75', width=57.86):
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='76', width=57.86):
            with Note(default_x=16.87, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='77', width=61.79):
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.09, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=66.62):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=96.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.72, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.55, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=52.38, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.21, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='80', width=143.26):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.05, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=60.1, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.83, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='81', width=225.36):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=96.01, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=131.49, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=166.98, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.37, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='82', width=143.35):
            with Note(default_x=14.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=49.49, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=84.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=113.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='83', width=112.12):
            with Note(default_x=17.23, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=40.55, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=87.2, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='84', width=167.49):
            with Note(default_x=17.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.98, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=76.72, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.25, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='85', width=145.53):
            with Note(default_x=12.0, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.28, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=85.89, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.91, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='86', width=217.24):
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.76, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=115.72, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.68, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='87', width=252.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.32, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=165.43, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=204.55, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='88', width=206.25):
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.44, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='89', width=177.37):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=51.11, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=90.23, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.34, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='90', width=206.25):
            with Note(default_x=15.8, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=63.01, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=110.23, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.44, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='91', width=168.63):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.39, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-80.0)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-80.0)
            with Note(default_x=88.98, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.57, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
        with Measure(number='92', width=199.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='93', width=171.43):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.19, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.58, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.97, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='94', width=127.58):
            with Note(default_x=15.44, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='95', width=171.43):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=15.44, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='96', width=127.94):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='97', width=110.86):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=39.17, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=85.9, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='98', width=102.5):
            with Note(default_x=15.8, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=36.45, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.74, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='99', width=171.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=106.92, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=146.34, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='100', width=99.7):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=35.51, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=74.94, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='101', width=61.44):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.92, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='102', width=62.47):
            with Note(default_x=12.0, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='103', width=80.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=46.47, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=100.08):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.11, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=54.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='105', width=73.6):
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.9, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='106', width=74.65):
            with Note(default_x=21.03, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.04, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='107', width=78.67):
            with Note(default_x=12.0, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.91, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='108', width=100.08):
            with Note(default_x=12.0, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.11, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=54.21, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='109', width=108.44):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=35.71, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=59.42, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=83.13, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='110', width=136.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-155.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='111', width=77.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=52.95, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='112', width=94.95):
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='113', width=60.48):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=35.44, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='114', width=65.71):
            with Note(default_x=17.23, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=40.67, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='115', width=78.44):
            with Note(default_x=12.72, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.92, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.67, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='116', width=94.95):
            with Note(default_x=12.0, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='117', width=94.95):
            with Note(default_x=12.0, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.39, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=50.79, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.18, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='118', width=94.95):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='119', width=109.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.51, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.23, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.94, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='120', width=102.93):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.59, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.37, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=78.16, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='121', width=181.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=107.09, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=126.97, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.86, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='122', width=99.64):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.87, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='123', width=57.07):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='124', width=57.07):
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='125', width=57.03):
            with Note(default_x=12.36, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='126', width=83.06):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='127', width=109.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=35.68, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.57, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=75.45, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='128', width=103.44):
            with Note(default_x=15.8, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=36.76, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=57.71, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=78.67, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='129', width=106.03):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=51.77, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.65, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='130', width=99.64):
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.87, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='131', width=57.07):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='132', width=130.3):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='133', width=67.25):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='134', width=67.25):
            with Note(default_x=15.8, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='135', width=67.25):
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='136', width=67.25):
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='137', width=67.25):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='138', width=152.78):
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=58.22, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.49, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.75, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=128.02, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='139', width=127.7):
            with Note(default_x=15.8, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='140', width=73.14):
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='141', width=190.91):
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.28, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.76, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.23, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.71, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.19, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.67, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.14, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='142', width=458.91):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.47, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.0, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.26, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=318.52, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.79, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.05, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='143', width=271.57):
            with Note(default_x=15.8, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.89, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='144', width=280.61):
            with Note(default_x=15.8, default_y=-100.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=177.45):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(40.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(-1)
                    Chromatic(-2.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=108.26, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.6, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=106.4):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.69, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=63.96):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.18, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=65.96):
            with Note(default_x=13.64, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='5', width=89.53):
            with Note(default_x=15.8, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='6', width=106.4):
            with Note(default_x=15.8, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.69, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=98.42):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=53.1, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=64.99):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='9', width=81.19):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=39.34, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='10', width=106.4):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=59.69, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='11', width=152.65):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=121.68, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=66.17):
            with Note(default_x=16.87, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='13', width=145.7):
            with Note(default_x=15.44, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='14', width=108.88):
            with Note(default_x=15.8, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.09, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=91.22):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=48.31, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=57.79):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='17', width=218.82):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=112.22, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='18', width=74.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=44.86, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='19', width=95.77):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='20', width=201.36):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.76, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=144.66, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=172.21, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='21', width=238.09):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=123.24, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='22', width=93.37):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=8.58, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=17.23, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.5, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='23', width=115.04):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='24', width=82.3):
            with Note(default_x=17.23, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='25', width=165.01):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-54.12, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-89.12)
            with Note(default_x=15.8, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=94.61, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='26', width=115.92):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=65.06, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='27', width=228.3):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-61.97, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='diminuendo', number=1, default_y=-96.97)
            with Note(default_x=91.01, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=171.67, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='28', width=98.83):
            with Note(default_x=15.8, default_y=-270.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=54.65, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='29', width=141.51):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='30', width=89.96):
            with Note(default_x=15.44, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='31', width=90.26):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='32', width=119.73):
            with Note(default_x=15.8, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=41.38, default_y=-275.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=66.97, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=92.55, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='33', width=95.76):
            with Note(default_x=12.72, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.14, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=51.57, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=70.99, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='34', width=146.73):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=38.66, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=71.98, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=105.3, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=251.09):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=164.31, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='36', width=204.76):
            with Note(default_x=15.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.48, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='37', width=179.68):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.91, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='38', width=204.76):
            with Note(default_x=15.8, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=109.48, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='39', width=170.81):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='40', width=154.09):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=113.65, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='41', width=93.03):
            with Note(default_x=12.72, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=31.24, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=49.75, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.27, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='42', width=108.69):
            with Note(default_x=12.72, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.37, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.27, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=83.92, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='43', width=58.88):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='44', width=92.31):
            with Note(default_x=12.0, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=67.55, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='45', width=92.31):
            with Note(default_x=12.0, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.52, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=49.03, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.55, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='46', width=97.54):
            with Note(default_x=17.23, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=54.26, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='47', width=63.08):
            with Note(default_x=17.23, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.31, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='48', width=66.68):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=41.92, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='49', width=93.03):
            with Note(default_x=12.72, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=31.24, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=49.75, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=68.27, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='50', width=91.46):
            with Note(default_x=12.72, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.79, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=66.69, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='51', width=177.06):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=108.9, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=130.6, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=152.3, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='52', width=101.86):
            with Note(default_x=12.0, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=77.09, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='53', width=101.86):
            with Note(default_x=12.0, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=33.7, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=55.4, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=77.09, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='54', width=107.09):
            with Note(default_x=17.23, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=60.63, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='55', width=72.63):
            with Note(default_x=17.23, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=44.13, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='56', width=76.23):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=51.46, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='57', width=102.58):
            with Note(default_x=12.72, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=34.42, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=56.12, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.81, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='58', width=101.0):
            with Note(default_x=12.72, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=46.34, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=76.24, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='59', width=170.79):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=31.15, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=50.29, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.44, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=88.58, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.73, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.88, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=146.02, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='60', width=242.71):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=105.88, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.56, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.24, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=161.91, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=180.59, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.27, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.94, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='61', width=150.27):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=39.52, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=56.71, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=73.91, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=91.11, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.31, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.5, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='62', width=111.74):
            with Note(default_x=12.0, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(20.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=77.37, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='63', width=98.93):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='64', width=98.93):
            with Note(default_x=12.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    with Ornaments():
                        TrillMark()
        with Measure(number='65', width=76.27):
            with Note(default_x=15.8, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.23, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='66', width=76.21):
            with Note(default_x=12.0, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=43.3, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=76.27):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=45.23, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='68', width=79.76):
            with Note(default_x=12.0, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=45.08, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='69', width=167.13):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.41)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Direction(placement='above'):
                with DirectionType():
                    with Dynamics(default_x=6.58, relative_x=-3.88, relative_y=16.01):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=87.21, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='70', width=63.18):
            with Note(default_x=12.0, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='71', width=79.74):
            with Note(default_x=12.36, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='72', width=63.54):
            with Note(default_x=12.36, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='73', width=73.95):
            with Note(default_x=15.44, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='74', width=79.18):
            with Note(default_x=20.67, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
        with Measure(number='75', width=57.86):
            with Note(default_x=12.0, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='76', width=57.86):
            with Note(default_x=16.87, default_y=-250.41):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='77', width=61.79):
            with Note(default_x=12.0, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=36.09, default_y=-280.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='78', width=66.62):
            with Note(default_x=15.8, default_y=-280.41):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='79', width=96.98):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.72, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.55, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=52.38, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.21, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='80', width=143.26):
            with Note(default_x=12.0, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=36.05, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=60.1, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=102.83, default_y=-245.41):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='81', width=225.36):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=96.01, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.49, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=166.98, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=195.37, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='82', width=143.35):
            with Note(default_x=14.0, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=49.49, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=84.97, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=113.36, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='83', width=112.12):
            with Note(default_x=17.23, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=40.55, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=63.88, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=87.2, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='84', width=167.49):
            with Note(default_x=17.23, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.98, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=76.72, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=123.25, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='85', width=145.53):
            with Note(default_x=12.0, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.28, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=85.89, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.91, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='86', width=217.24):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=65.76, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=115.72, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=165.68, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='87', width=252.58):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=126.32, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=165.43, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=204.55, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='88', width=206.25):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=63.01, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=110.23, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=157.44, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='89', width=177.37):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.11, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.23, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=129.34, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='90', width=206.25):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=63.01, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=110.23, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=157.44, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='91', width=168.63):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.39, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('cresc.', font_family='FreeSerif', font_size='12', font_style='italic', default_y=-90.98)
                with DirectionType():
                    Dashes(type='start', number=1, default_y=-90.98)
            with Note(default_x=88.98, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=125.57, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Dashes(type='stop', number=1)
        with Measure(number='92', width=199.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.57, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=115.11, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=142.66, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=170.2, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='93', width=171.43):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.19, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.58, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.97, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='94', width=127.58):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.35, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=70.89, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=98.44, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='95', width=171.43):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-93.83)
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.19, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=90.58, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=127.97, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='96', width=127.94):
            with Note(default_x=16.16, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=43.71, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=71.25, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=98.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='97', width=110.86):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_x=23.84, relative_y=-50.98):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=62.53, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='98', width=102.5):
            with Note(default_x=15.8, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=57.09, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='99', width=171.11):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.63, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='100', width=99.7):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=55.22, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='101', width=61.44):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=35.92, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='102', width=62.47):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='103', width=80.84):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Mp()
                Sound(dynamics=71.11)
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=46.47, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='104', width=100.08):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.11, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=54.21, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='105', width=73.6):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=43.9, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='106', width=74.65):
            with Note(default_x=21.03, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=47.04, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='107', width=78.67):
            with Note(default_x=12.0, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=37.79, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=53.91, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='108', width=100.08):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=33.11, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=54.21, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.32, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='109', width=108.44):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=35.71, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=59.42, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=83.13, default_y=-265.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='110', width=136.72):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='111', width=77.71):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        P()
                Sound(dynamics=54.44)
            with Note(default_x=12.0, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=37.2, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='112', width=94.95):
            with Note(default_x=12.0, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.79, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='113', width=60.48):
            with Note(default_x=12.0, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=35.44, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='114', width=65.71):
            with Note(default_x=16.87, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='115', width=78.44):
            with Note(default_x=12.36, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='116', width=94.95):
            with Note(default_x=12.0, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=50.79, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='117', width=94.95):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=50.79, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='118', width=94.95):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='119', width=109.32):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        F()
                Sound(dynamics=106.67)
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=74.94, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='120', width=102.93):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=36.59, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=57.37, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='121', width=181.23):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=146.86, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='122', width=99.64):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='123', width=57.07):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='124', width=57.07):
            with Note(default_x=12.36, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='125', width=57.03):
            with Note(default_x=12.36, default_y=-230.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='126', width=83.06):
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-75.0)
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
        with Measure(number='127', width=109.83):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=6.58, default_y=-40.0, relative_y=-40.0):
                        Ff()
                Sound(dynamics=124.44)
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=75.45, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='128', width=103.44):
            with Note(default_x=15.8, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=36.76, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=57.71, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='129', width=106.03):
            with Note(default_x=12.0, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(60.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=71.65, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='130', width=99.64):
            with Note(default_x=12.0, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=32.96, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(20.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=53.91, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='131', width=57.07):
            with Note(default_x=15.8, default_y=-235.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='132', width=130.3):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='133', width=67.25):
            with Note(default_x=12.36, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='134', width=67.25):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='135', width=67.25):
            with Note(default_x=12.36, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='136', width=67.25):
            with Note(default_x=12.36, default_y=-245.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='137', width=67.25):
            with Note(default_x=12.36, default_y=-240.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(80.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='138', width=152.78):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='139', width=127.7):
            with Note(default_x=15.8, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=52.67, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=69.42, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.18, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.94, default_y=-220.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='140', width=73.14):
            with Note(default_x=12.94, default_y=-225.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
        with Measure(number='141', width=190.91):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.28, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.76, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.23, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.71, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.19, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.67, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.14, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='142', width=458.91):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=87.21, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.47, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.73, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.0, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=272.26, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=318.52, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=364.79, default_y=-250.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=411.05, default_y=-255.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(10.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='143', width=271.57):
            with Note(default_x=15.8, default_y=-260.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=142.89, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='144', width=280.61):
            with Note(default_x=15.8, default_y=-215.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(40.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(40.0)
                Voice('1')
                Type('quarter')
            with Barline(location='right'):
                BarStyle('light-heavy')