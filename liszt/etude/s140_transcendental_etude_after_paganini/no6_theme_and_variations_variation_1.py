with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('h')
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
        CreditWords('Impossible Franz Liszt S. 140 Etude 6\n', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
        CreditWords(None)
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Franz Liszt', default_x=1134.19, default_y=1526.67, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Variation 1', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('none')
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
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=424.12):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(218.33)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(65.0)
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Attributes():
                Divisions(12.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('2')
                    BeatType('4')
                Staves(3)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('G')
                    Line(2)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    Words('Var. 1', default_y=20.33, relative_y=80.0, font_weight='bold', font_size='13')
                Staff(1)
            with Note(default_x=100.26, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=100.26, default_y=45.0):
                Grace()
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=111.22, default_y=20.0):
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
            with Note(default_x=111.22, default_y=55.0):
                Grace()
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=122.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=122.94, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.94, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.94, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.94, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.94, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=159.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=159.4, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=159.4, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=159.4, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=159.4, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=159.4, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=212.43, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.43, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.43, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.43, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.43, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.51, default_y=-25.0):
                with Pitch():
                    Step('A')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=266.51, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.51, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.51, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.51, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.51, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=315.41, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=315.41, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=315.41, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=315.41, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=315.41, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=315.41, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=368.44, default_y=-50.0):
                with Pitch():
                    Step('C')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=368.44, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=368.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=368.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=368.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=368.44, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=122.94, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=122.94, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=122.94, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=122.94, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=234.17, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=234.17, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=234.17, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=234.17, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=266.51, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=266.51, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=266.51, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=266.51, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=298.84, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.84, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=298.84, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=298.84, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.93, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.93, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.93, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.93, default_y=-205.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=390.19, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=390.19, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=390.19, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=390.19, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
        with Measure(number='2', width=335.77):
            with Note(default_x=13.8, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=13.8, default_y=30.0):
                Grace()
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=39.19, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=39.19, default_y=40.0):
                Grace()
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=50.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=50.9, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=50.9, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=50.9, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=50.9, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=50.9, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=86.61, default_y=-20.0):
                with Pitch():
                    Step('B')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=86.61, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=86.61, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=86.61, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=86.61, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=86.61, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.55, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=138.55, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.55, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.55, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.55, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.55, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=186.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=186.44, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=186.44, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=186.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=186.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=186.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=234.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
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
                        Staccatissimo()
            with Note(default_x=234.34, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=234.34, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=234.34, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=234.34, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=234.34, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=286.27, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=286.27, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=286.27, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=286.27, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=286.27, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Note(default_x=286.27, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=50.9, default_y=-260.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=50.9, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=50.9, default_y=-190.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=154.78, default_y=-295.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=154.78, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=154.78, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=186.44, default_y=-295.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=186.44, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=186.44, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=218.11, default_y=-285.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=218.11, default_y=-250.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=218.11, default_y=-215.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(3)
            with Note(default_x=260.3, default_y=-290.0):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.3, default_y=-255.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=260.3, default_y=-220.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=302.5, default_y=-295.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=302.5, default_y=-260.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=302.5, default_y=-225.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
        with Measure(number='3', width=317.61):
            with Note(default_x=13.8, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(5)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=13.8, default_y=45.0):
                Grace()
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=24.77, default_y=20.0):
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
            with Note(default_x=24.77, default_y=55.0):
                Grace()
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=36.48, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=36.48, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=36.48, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=36.48, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=36.48, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=36.48, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=71.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=71.72, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=71.72, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=71.72, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=71.72, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=71.72, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.97, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=122.97, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.97, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.97, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.97, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=122.97, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=170.23, default_y=-25.0):
                with Pitch():
                    Step('A')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=170.23, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=170.23, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=170.23, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=170.23, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=170.23, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.49, default_y=-40.0):
                with Pitch():
                    Step('E')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=217.49, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.49, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.49, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.49, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.49, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=268.74, default_y=-50.0):
                with Pitch():
                    Step('C')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=268.74, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=268.74, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=268.74, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=268.74, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=268.74, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=36.48, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=36.48, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=36.48, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=36.48, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=138.98, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=138.98, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=138.98, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=138.98, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=170.23, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=170.23, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=170.23, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=170.23, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=201.48, default_y=-305.0):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.48, default_y=-270.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=201.48, default_y=-235.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=201.48, default_y=-200.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=243.12, default_y=-310.0):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.12, default_y=-275.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=243.12, default_y=-240.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=243.12, default_y=-205.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=284.76, default_y=-315.0):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=284.76, default_y=-280.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=284.76, default_y=-245.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=284.76, default_y=-210.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
        with Measure(number='4', width=394.18):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(192.72)
                with StaffLayout(number=2):
                    StaffDistance(69.4)
                with StaffLayout(number=3):
                    StaffDistance(102.55)
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=96.43)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=107.28, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=107.28, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=107.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=107.28, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=107.28, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=107.28, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=153.19, default_y=-20.0):
                with Pitch():
                    Step('B')
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
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=153.19, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=153.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=153.19, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=153.19, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=153.19, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=216.62, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.62, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=61.37, default_y=-301.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='below', number=1)
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=61.37, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=61.37, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=153.19, default_y=-336.95):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=153.19, default_y=-301.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=153.19, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(3)
            with Attributes():
                with Clef(number=3):
                    Sign('G')
                    Line(2)
            with Note(default_x=216.62, default_y=-326.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=216.62, default_y=-291.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=216.62, default_y=-256.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=262.53, default_y=-361.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=262.53, default_y=-326.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=262.53, default_y=-291.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note(default_x=329.91, default_y=-336.95):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=329.91, default_y=-301.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=329.91, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='5', width=275.67):
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=96.43)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='crescendo', number=1, default_y=-96.7)
                Staff(1)
            with Note(default_x=55.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=55.44, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.44, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.44, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.44, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.44, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=97.09, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=97.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=97.09, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=97.09, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=97.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=97.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=138.73, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Direction(placement='below'):
                with DirectionType():
                    Wedge(type='stop', number=1)
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-266.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Tuplet(type='start', bracket='yes')
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=13.8, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=97.09, default_y=-301.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Tuplet(type='stop')
                    Slur(type='stop', number=1)
            with Note(default_x=97.09, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                    NormalType('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=138.73, default_y=-336.95):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=138.73, default_y=-301.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=180.37, default_y=-301.95):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=180.37, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Note(default_x=232.43, default_y=-266.95):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=232.43, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('up')
                Staff(3)
            with Barline(location='right'):
                Ending(None, number='2', type='discontinue')
        with Measure(number='6', width=407.64):
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='down', size=8, number=1, default_y=79.72)
                Staff(1)
            with Note(default_x=26.17, default_y=-15.0):
                Grace()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=26.17, default_y=20.0):
                Grace()
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Note(default_x=37.14, default_y=-5.0):
                Grace()
                with Pitch():
                    Step('E')
                    Octave(6)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=37.14, default_y=30.0):
                Grace()
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=48.85, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
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
            with Note(default_x=48.85, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=48.85, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=48.85, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=48.85, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=48.85, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=92.79, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.79, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.79, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.79, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.79, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(5)
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
            with Note(default_x=156.7, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Direction(placement='above'):
                with DirectionType():
                    OctaveShift(type='stop', size=8, number=1)
                Staff(1)
            with Note(default_x=215.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=215.64, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=215.64, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=215.64, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=215.64, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=215.64, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=274.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=274.57, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=274.57, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=274.57, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=338.48, default_y=-40.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=338.48, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=338.48, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=338.48, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=48.85, default_y=-356.95):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=48.85, default_y=-321.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=48.85, default_y=-286.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=48.85, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=48.85, default_y=-216.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=176.67, default_y=-321.95):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=176.67, default_y=-286.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=176.67, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=176.67, default_y=-216.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.64, default_y=-321.95):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=215.64, default_y=-286.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.64, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.64, default_y=-216.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=254.6, default_y=-316.95):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.6, default_y=-281.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(3)
            with Note(default_x=254.6, default_y=-246.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(3)
            with Note(default_x=254.6, default_y=-211.95):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(3)
            with Note(default_x=306.53, default_y=-321.95):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.53, default_y=-286.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=306.53, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=306.53, default_y=-216.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=358.46, default_y=-326.95):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=358.46, default_y=-291.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=358.46, default_y=-256.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=358.46, default_y=-221.95):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=124.75, default_y=-356.95):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-346.95):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-336.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-321.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-311.95):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-301.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-286.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-276.95):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-266.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-251.95):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-241.95):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note(default_x=124.75, default_y=-231.95):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=25.51)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='7', width=291.63):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(90.5)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(97.55)
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=88.89, default_y=-35.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=88.89, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=88.89, default_y=-10.0):
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
            with Note(default_x=88.89, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=88.89, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=88.89, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=128.91, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=128.91, default_y=-10.0):
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
            with Note(default_x=128.91, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=128.91, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=128.91, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=128.91, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=-10.0):
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
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=169.88, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=169.88, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=209.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=209.94, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=209.94, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=209.94, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=209.94, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=209.94, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=249.96, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
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
            with Note(default_x=249.96, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=249.96, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=249.96, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=249.96, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=249.96, default_y=70.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=61.37, default_y=-322.55):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=61.37, default_y=-287.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=61.37, default_y=-252.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=61.37, default_y=-217.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=144.58, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=144.58, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=144.58, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=144.58, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=169.88, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=169.88, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=169.88, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=169.88, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.28, default_y=-322.55):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.28, default_y=-287.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.28, default_y=-252.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.28, default_y=-217.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=229.95, default_y=-327.55):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=229.95, default_y=-292.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=229.95, default_y=-257.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=229.95, default_y=-222.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=265.63, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=265.63, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=265.63, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=265.63, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=108.9, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=108.9, default_y=-312.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=108.9, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=108.9, default_y=-277.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=108.9, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=108.9, default_y=-242.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='8', width=259.47):
            with Note(default_x=23.09, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(5)
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
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=23.09, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=23.09, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=23.09, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=23.09, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=23.09, default_y=75.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=80.51)
            with Note(default_x=51.24, default_y=5.0):
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
                Beam('continue', number=1)
            with Note(default_x=51.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=51.24, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=51.24, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=51.24, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=51.24, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.19, default_y=-10.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=92.19, default_y=5.0):
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
            with Note(default_x=92.19, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.19, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=92.19, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=135.66, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=135.66, default_y=-10.0):
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
            with Note(default_x=135.66, default_y=5.0):
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
            with Note(default_x=135.66, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=135.66, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=135.66, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=176.29, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=176.29, default_y=-10.0):
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
            with Note(default_x=176.29, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=176.29, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.24, default_y=-45.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=217.24, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=217.24, default_y=-10.0):
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
            with Note(default_x=217.24, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=23.09, default_y=-317.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=23.09, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=23.09, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=23.09, default_y=-212.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=107.86, default_y=-317.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=107.86, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=107.86, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=107.86, default_y=-212.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=135.66, default_y=-317.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=135.66, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=135.66, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=135.66, default_y=-212.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=160.62, default_y=-312.55):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.62, default_y=-277.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=160.62, default_y=-242.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=160.62, default_y=-207.55):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=196.76, default_y=-317.55):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.76, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=196.76, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=196.76, default_y=-212.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=232.91, default_y=-322.55):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=232.91, default_y=-287.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=232.91, default_y=-252.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=232.91, default_y=-217.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=71.72, default_y=-342.55):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-332.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-322.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-307.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-287.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-272.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-252.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-237.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note(default_x=71.72, default_y=-217.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=30.51)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='9', width=246.81):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Staff(1)
                with Notations():
                    Tuplet(type='start', bracket='yes')
            with Note(default_x=41.36, default_y=-40.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=41.36, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=41.36, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=41.36, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=41.36, default_y=5.0):
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
            with Note(default_x=41.36, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=81.45, default_y=-30.0):
                with Pitch():
                    Step('G')
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
            with Note(default_x=81.45, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=81.45, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=81.45, default_y=5.0):
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
            with Note(default_x=81.45, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=81.45, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=124.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
            with Note(default_x=124.91, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=124.91, default_y=5.0):
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
            with Note(default_x=124.91, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=124.91, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=124.91, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=165.02, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=165.02, default_y=5.0):
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
            with Note(default_x=165.02, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=165.02, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=165.02, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=165.02, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=205.1, default_y=5.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=205.1, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=205.1, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=205.1, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=205.1, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=205.1, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-327.55):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-292.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-257.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-222.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=97.11, default_y=-337.55):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=97.11, default_y=-302.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=97.11, default_y=-267.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=97.11, default_y=-232.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=124.91, default_y=-337.55):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=124.91, default_y=-302.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=124.91, default_y=-267.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=124.91, default_y=-232.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=149.35, default_y=-327.55):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.35, default_y=-292.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=149.35, default_y=-257.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=149.35, default_y=-222.55):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=185.06, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=185.06, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=185.06, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=185.06, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=220.77, default_y=-337.55):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=220.77, default_y=-302.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=220.77, default_y=-267.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=220.77, default_y=-232.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=61.4, default_y=-337.55):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=61.4, default_y=-317.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=61.4, default_y=-302.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=61.4, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=61.4, default_y=-267.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note(default_x=61.4, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=0.51)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='10', width=279.58):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-40.0, relative_y=-40.0):
                        Rfz()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=32.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
                    with Articulations():
                        Accent()
            with Note(default_x=32.9, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=21.03, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=32.9, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=32.9, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=32.9, default_y=70.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=56.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=68.03, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=68.03, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=56.16, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=68.03, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=68.03, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=110.59, default_y=-10.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=110.59, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=110.59, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=110.59, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=110.59, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=110.59, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=152.2, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=152.2, default_y=-10.0):
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
            with Note(default_x=152.2, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=152.2, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=152.2, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=152.2, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=193.81, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=193.81, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=181.95, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=193.81, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=193.81, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=193.81, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=224.5, default_y=-35.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=236.37, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=236.37, default_y=-10.0):
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
            with Note(default_x=224.5, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=236.37, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=236.37, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=32.9, default_y=-322.55):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=32.9, default_y=-287.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=32.9, default_y=-252.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=32.9, default_y=-217.55):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=126.25, default_y=-342.55):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=126.25, default_y=-307.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=126.25, default_y=-272.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=126.25, default_y=-237.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=152.2, default_y=-342.55):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=152.2, default_y=-307.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=152.2, default_y=-272.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=152.2, default_y=-237.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.15, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=178.15, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.15, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.15, default_y=-227.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.09, default_y=-337.55):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.09, default_y=-302.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.09, default_y=-267.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=215.09, default_y=-232.55):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=252.04, default_y=-342.55):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=252.04, default_y=-307.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=252.04, default_y=-272.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=252.04, default_y=-237.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=89.31, default_y=-332.55):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-317.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-307.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-297.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-282.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-272.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-262.55):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-247.55):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note(default_x=89.31, default_y=-237.55):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=10.51)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='11', width=377.64):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(170.31)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
                with StaffLayout(number=3):
                    StaffDistance(71.82)
            with Note(default_x=64.11, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
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
                    with Articulations():
                        Accent()
            with Note(default_x=64.11, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=64.11, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=64.11, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=64.11, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=64.11, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.43, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=103.43, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.43, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.43, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.43, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.43, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
            with Note(default_x=160.62, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.62, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.62, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.62, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=160.62, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=213.36, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=213.36, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=213.36, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=213.36, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=213.36, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=213.36, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.1, default_y=-40.0):
                with Pitch():
                    Step('E')
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
            with Note(default_x=266.1, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.1, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.1, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.1, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=266.1, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=323.29, default_y=-50.0):
                with Pitch():
                    Step('C')
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
            with Note(default_x=323.29, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=323.29, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=323.29, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=323.29, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=323.29, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=64.11, default_y=-301.82):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.11, default_y=-266.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.11, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.11, default_y=-196.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Staff(3)
            with Note(default_x=178.49, default_y=-321.82):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.49, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.49, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=178.49, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=213.36, default_y=-321.82):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.36, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=213.36, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=213.36, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=248.23, default_y=-311.82):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=248.23, default_y=-276.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=248.23, default_y=-241.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=248.23, default_y=-206.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=294.7, default_y=-316.82):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.7, default_y=-281.82):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=294.7, default_y=-246.82):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=294.7, default_y=-211.82):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.17, default_y=-321.82):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=341.17, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.17, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=341.17, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=132.02, default_y=-311.82):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-301.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-276.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-266.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-241.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=132.02, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(12.0)
                Voice('10')
                Type('quarter')
                Staff(3)
        with Measure(number='12', width=329.44):
            with Note(default_x=13.8, default_y=-45.0):
                with Pitch():
                    Step('D')
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
            with Note(default_x=13.8, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-10.0):
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
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=-35.0):
                with Pitch():
                    Step('F')
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
            with Note(default_x=55.17, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=-10.0):
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
            with Note(default_x=55.17, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=55.17, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.47, default_y=-25.0):
                with Pitch():
                    Step('A')
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
            with Note(default_x=115.33, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=115.33, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.47, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=115.33, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=115.33, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=103.47, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=115.33, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=115.33, default_y=70.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tuplet(type='start', bracket='no')
            with Note(default_x=156.7, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=156.7, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=-20.0):
                with Pitch():
                    Step('B')
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
            with Note(default_x=212.19, default_y=-10.0):
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
            with Note(default_x=212.19, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=40.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=212.19, default_y=75.0):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=260.49, default_y=-10.0):
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
                Beam('end', number=1)
                with Notations():
                    Tuplet(type='stop')
            with Note(default_x=272.35, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=272.35, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=260.49, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=272.35, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=272.35, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=260.49, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=272.35, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=272.35, default_y=85.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=13.8, default_y=-296.82):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=13.8, default_y=-261.82):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-226.82):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=85.25, default_y=-271.82):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=85.25, default_y=-236.82):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=85.25, default_y=-201.82):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=156.7, default_y=-266.82):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.7, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=193.38, default_y=-231.82):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.38, default_y=-196.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=253.44, default_y=-236.82):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.44, default_y=-201.82):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=291.16, default_y=-246.82):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=291.16, default_y=-211.82):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(24.0)
            with Note(default_x=29.97, default_y=-306.82):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=29.97, default_y=-271.82):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=29.97, default_y=-236.82):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Staff(3)
            with Note(default_x=156.7, default_y=-301.82):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('begin', number=1)
            with Note(default_x=156.7, default_y=-266.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=242.27, default_y=-301.82):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
                Beam('end', number=1)
            with Note(default_x=242.27, default_y=-291.82):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=242.27, default_y=-266.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=242.27, default_y=-256.82):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
            with Note(default_x=242.27, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Stem('down')
                Staff(3)
            with Note(default_x=242.27, default_y=-221.82):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('10')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(3)
        with Measure(number='13', width=231.11):
            with Note(default_x=23.09, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
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
            with Note(default_x=23.09, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=23.09, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=23.09, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=23.09, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=23.09, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=59.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=59.29, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=59.29, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=59.29, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=59.29, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=59.29, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=95.49, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
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
            with Note(default_x=95.49, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=95.49, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=95.49, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=95.49, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=95.49, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                with TimeModification():
                    ActualNotes(3)
                    NormalNotes(2)
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=131.7, default_y=80.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note(default_x=23.09, default_y=-321.82):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        StrongAccent(type='up')
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=23.09, default_y=-301.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=23.09, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=23.09, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=23.09, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Note(default_x=23.09, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=5.51)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-139.61)
                Staff(3)
            with Note(default_x=131.7, default_y=-311.82):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=131.7, default_y=-301.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-286.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-276.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-266.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-251.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-241.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-231.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-216.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-206.82):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-196.82):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=131.7, default_y=-181.82):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(6.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='14', width=139.3):
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(24.0)
            with Note():
                Rest(measure='yes')
                Duration(24.0)
                Voice('9')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')