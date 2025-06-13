with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('k 2')
        WorkTitle('Minuet')
    with Identification():
        Creator('Wolfgang Amadeus Mozart', type='composer')
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
        CreditWords('Minuet', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('k 2', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Wolfgang Amadeus Mozart', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName(None)
            with ScoreInstrument(id='P1-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName(None)
            with ScoreInstrument(id='P2-I1'):
                InstrumentName(None)
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(1)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=186.06):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(170.0)
            with Attributes():
                Divisions(6.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.36, default_y=3.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('132')
                Sound(tempo=132.0)
            with Note(default_x=101.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=117.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=133.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=159.02, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=94.99):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=98.43):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=45.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.39, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=76.61):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=51.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=98.06):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=29.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=45.59, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='6', width=98.06):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=29.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=45.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='7', width=116.08):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=29.47, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=45.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=60.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=96.82):
            with Note(default_x=13.44, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=55.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=117.4):
            with Note(default_x=17.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.82, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=63.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=89.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='10', width=94.99):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=181.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.38, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=97.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=126.93, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=153.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=84.3):
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=59.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=95.8):
            with Note(default_x=10.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.78, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.83, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='14', width=95.8):
            with Note(default_x=10.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.78, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=68.52, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=95.08):
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=26.05, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=42.11, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=67.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=77.43):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=52.66, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=95.8):
            with Note(default_x=10.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='18', width=95.8):
            with Note(default_x=10.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.78, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.83, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='19', width=99.24):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=30.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=46.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=71.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=60.6):
            with Note(default_x=10.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=35.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='21', width=95.8):
            with Note(default_x=10.72, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=26.78, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=42.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=68.52, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='22', width=407.82):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=80.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=205.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=306.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='23', width=341.24):
            with Note(default_x=14.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=139.35, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=239.5, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=328.43):
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=215.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=186.06):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(6.0)
                with Key():
                    Fifths(-1)
                    Mode('major')
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=101.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=159.02, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='2', width=94.99):
            with Note(default_x=10.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=67.95, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=98.43):
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=71.39, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=76.61):
            with Note(default_x=10.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.1, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.84, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='5', width=98.06):
            with Note(default_x=13.44, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='6', width=98.06):
            with Note(default_x=13.44, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='7', width=116.08):
            with Note(default_x=13.8, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=60.8, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.64, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=96.82):
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=34.54, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=55.28, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='9', width=117.4):
            with Note(default_x=17.59, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
        with Measure(number='10', width=94.99):
            with Note(default_x=10.36, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='11', width=181.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=126.93, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=153.58, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='12', width=84.3):
            with Note(default_x=17.23, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=38.38, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.53, default_y=-145.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=95.8):
            with Note(default_x=10.36, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='14', width=95.8):
            with Note(default_x=10.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='15', width=95.08):
            with Note(default_x=10.0, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=42.11, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=67.79, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=77.43):
            with Note(default_x=10.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=31.51, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=52.66, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=95.8):
            with Note(default_x=10.36, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='18', width=95.8):
            with Note(default_x=10.36, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='19', width=99.24):
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=71.96, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='20', width=60.6):
            with Note(default_x=10.36, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
        with Measure(number='21', width=95.8):
            with Note(default_x=10.36, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='22', width=407.82):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=80.38, default_y=-100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(18.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='23', width=341.24):
            with Note(default_x=13.8, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=239.5, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='24', width=328.43):
            with Note(default_x=10.36, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.85, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=215.34, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')