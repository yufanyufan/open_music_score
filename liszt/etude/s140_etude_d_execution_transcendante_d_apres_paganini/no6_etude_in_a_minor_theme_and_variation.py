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
        CreditWords('h', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
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
        with Measure(number='1', width=267.97):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(192.72)
                with StaffLayout(number=2):
                    StaffDistance(230.73)
                with StaffLayout(number=3):
                    StaffDistance(145.4)
            with Attributes():
                Divisions(8.0)
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
                    Sign('C')
                    Line(3)
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-39.8, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=7.5, default_y=-40.0, relative_y=-40.0):
                        Mf()
                Staff(1)
                Sound(dynamics=88.89)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=87.17, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-385.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-360.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-290.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-255.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-185.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=87.17, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=148.52, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.52, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.78, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.78, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-395.73):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.43, default_y=-360.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-325.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-290.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-255.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-220.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-185.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=195.43, default_y=-150.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-400.73):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.08, default_y=-365.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-330.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-295.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-260.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-225.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-190.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=219.08, default_y=-155.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=242.73, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=242.73, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='2', width=241.42):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=34.12, default_y=-400.73):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-385.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-375.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-365.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-340.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-295.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-270.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-260.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-245.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-235.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-200.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-190.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-175.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-165.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-155.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=97.26, default_y=-385.73):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-245.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=97.26, default_y=-175.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-385.73):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=120.53, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-245.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=120.53, default_y=-175.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-375.73):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.83, default_y=-340.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-305.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-270.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-235.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-200.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.83, default_y=-165.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-380.73):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.14, default_y=-345.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-310.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-275.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-240.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-205.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=191.14, default_y=-170.73):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-385.73):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=215.48, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-245.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=215.48, default_y=-175.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='3', width=203.9):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-395.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-385.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-360.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-290.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-280.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-255.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-210.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-185.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=84.44, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.44, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=107.7, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.7, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-395.73):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=131.35, default_y=-360.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-325.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-290.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-255.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-220.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-185.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=131.35, default_y=-150.73):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-400.73):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.0, default_y=-365.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-330.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-295.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-260.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-225.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-190.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=155.0, default_y=-155.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=178.65, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=178.65, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
        with Measure(number='4', width=136.95):
            with Note(default_x=34.12, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=34.12, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=34.12, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=34.12, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=34.12, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=34.12, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=74.98, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Slur(type='stop', number=1)
                    with Articulations():
                        Staccatissimo()
                    with Ornaments():
                        TrillMark()
                        WavyLine(type='start', number=1, default_y=71.05)
            with Note(default_x=74.98, default_y=-110.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.98, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.98, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.98, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=74.98, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
                with Notations():
                    with Ornaments():
                        WavyLine(type='stop', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=34.12, default_y=-400.73):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-375.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-365.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-340.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-330.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-295.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-270.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-260.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-235.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-200.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-190.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-165.73):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note(default_x=34.12, default_y=-155.73):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=120.51)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=227.25):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=34.12, default_y=-405.73):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-395.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-385.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-370.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-360.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-350.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-315.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-290.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-245.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-220.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-185.73):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-175.73):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=96.17, default_y=-370.73):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=96.17, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-370.73):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=119.43, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=119.43, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-365.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.9, default_y=-330.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-295.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-260.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-225.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-190.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=153.9, default_y=-155.73):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-370.73):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.82, default_y=-335.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-300.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-265.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-230.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-195.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=177.82, default_y=-160.73):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-375.73):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=201.74, default_y=-340.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-305.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-270.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-235.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-200.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=201.74, default_y=-165.73):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='6', width=247.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(146.33)
                with StaffLayout(number=3):
                    StaffDistance(145.4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.31, default_y=-321.33):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-306.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-296.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-286.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-261.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-216.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-191.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-156.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-121.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-86.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=62.31, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=125.43, default_y=-306.33):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-131.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=125.43, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-306.33):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=148.7, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-131.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=148.7, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-296.33):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.03, default_y=-261.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-226.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-191.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-156.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-121.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=173.03, default_y=-86.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-301.33):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.36, default_y=-266.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-231.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-196.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-161.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-126.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=197.36, default_y=-91.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-306.33):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=221.69, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-131.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.69, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='7', width=208.4):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-306.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-291.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-256.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-221.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-116.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-81.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-71.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=86.21, default_y=-291.33):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-256.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-221.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-186.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-151.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-116.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-81.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-291.33):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=109.48, default_y=-256.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-221.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-186.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-151.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-116.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-81.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-286.33):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.81, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-216.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-291.33):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.14, default_y=-256.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-221.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-186.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-151.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-116.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-81.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-296.33):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.47, default_y=-261.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-226.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-191.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-156.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-121.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-86.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='8', width=208.4):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-301.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-291.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-266.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-256.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-221.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-196.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-186.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-161.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-151.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-126.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-116.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-91.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-81.33):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-66.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=86.21, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-171.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-136.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=109.48, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-171.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-136.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-301.33):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.81, default_y=-266.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-231.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-196.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-161.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-126.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-91.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-306.33):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.14, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-131.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.47, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-171.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-136.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='9', width=204.67):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-306.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-296.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-261.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-246.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-226.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-191.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-176.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-156.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-121.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-86.33):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note(default_x=23.09, default_y=-71.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=120.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=82.32, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-246.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-176.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=82.32, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('up')
                Staff(2)
            with Note(default_x=110.11, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=110.11, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.11, default_y=-246.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.11, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.11, default_y=-176.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.11, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.11, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-306.33):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.37, default_y=-271.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-236.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-201.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-166.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-131.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.37, default_y=-96.33):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.64, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-171.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-136.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.64, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.9, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-246.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-176.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=179.9, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='10', width=208.4):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-321.33):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-311.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-301.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-286.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-266.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-231.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-196.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-161.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-126.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-91.33):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=23.09, default_y=-66.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=86.21, default_y=-321.33):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-286.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-216.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=86.21, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-321.33):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=109.48, default_y=-286.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-216.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=109.48, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-311.33):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.81, default_y=-276.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-241.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-206.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-171.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-136.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-101.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=133.81, default_y=-66.33):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-316.33):
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.14, default_y=-281.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-246.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-211.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-176.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-141.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-106.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=158.14, default_y=-71.33):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-321.33):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.47, default_y=-286.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-251.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-216.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-181.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-146.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-111.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=182.47, default_y=-76.33):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='11', width=271.68):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(0.0)
                    TopSystemDistance(75.12)
                with StaffLayout(number=2):
                    StaffDistance(245.93)
                with StaffLayout(number=3):
                    StaffDistance(136.05)
            with Note(default_x=62.31, default_y=-395.93):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                    with Articulations():
                        StrongAccent(type='up')
            with Note(default_x=62.31, default_y=-360.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=62.31, default_y=-325.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=62.31, default_y=-290.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=62.31, default_y=-255.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=131.53, default_y=-80.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=131.53, default_y=-45.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=131.53, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=131.53, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=131.53, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=158.15, default_y=-400.93):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=2)
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=158.15, default_y=-365.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=158.15, default_y=-330.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=158.15, default_y=-295.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=158.15, default_y=-260.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=184.77, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.77, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=184.77, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=184.77, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=184.77, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=216.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=216.84, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=216.84, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=243.46, default_y=-90.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=243.46, default_y=-55.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=243.46, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=243.46, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=243.46, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(12.0)
            with Note(default_x=216.84, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.84, default_y=-75.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=216.84, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=93.04, default_y=-315.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=104.91, default_y=-310.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.04, default_y=-280.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.91, default_y=-275.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.04, default_y=-245.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.91, default_y=-240.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.04, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.91, default_y=-205.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=93.04, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.91, default_y=-170.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=216.84, default_y=-285.93):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=216.84, default_y=-275.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-250.93):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-240.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-205.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=216.84, default_y=-170.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(default_x=104.91, default_y=-566.98):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=116.77, default_y=-561.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=104.91, default_y=-531.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.77, default_y=-526.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=104.91, default_y=-496.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.77, default_y=-491.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(default_x=216.84, default_y=-536.98):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=216.84, default_y=-526.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=216.84, default_y=-501.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=216.84, default_y=-491.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=216.84, default_y=-466.98):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=216.84, default_y=-456.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
        with Measure(number='12', width=107.12):
            with Note(default_x=13.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=54.56, default_y=-420.93):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-400.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-385.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-365.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-350.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-330.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-315.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-295.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-280.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-270.93):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-245.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-235.93):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-200.93):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note(default_x=54.56, default_y=-165.93):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=125.51)
            with Note():
                Rest()
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-566.98):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-556.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-531.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-521.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-496.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-486.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-461.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-451.98):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Staff(3)
        with Measure(number='13', width=250.84):
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=130.37, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=130.37, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=130.37, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=34.12, default_y=-420.93):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Accent()
                        Staccatissimo()
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-400.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-385.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-375.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-350.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-330.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-315.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-305.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-260.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-245.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-235.93):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-190.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note(default_x=34.12, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-31.12, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=107.11, default_y=-245.93):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=107.11, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=107.11, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=130.37, default_y=-245.93):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=130.37, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.37, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=164.84, default_y=-240.93):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=164.84, default_y=-205.93):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=164.84, default_y=-170.93):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=192.98, default_y=-245.93):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=192.98, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=192.98, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.11, default_y=-250.93):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=221.11, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=221.11, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=130.37, default_y=-556.98):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=130.37, default_y=-546.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-531.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-521.98):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-511.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-496.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-486.98):
                Chord()
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-476.98):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=130.37, default_y=-461.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='14', width=227.48):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note(default_x=116.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=116.98, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=116.98, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-405.93):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                        Accent()
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-385.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-370.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-360.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-335.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-315.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-300.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-290.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-280.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-255.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-245.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-220.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-185.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note(default_x=23.09, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=115.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=93.72, default_y=-265.93):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=93.72, default_y=-230.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=93.72, default_y=-195.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=116.98, default_y=-265.93):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=116.98, default_y=-230.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=116.98, default_y=-195.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=144.21, default_y=-255.93):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=144.21, default_y=-220.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=144.21, default_y=-185.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.43, default_y=-260.93):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=171.43, default_y=-225.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=171.43, default_y=-190.93):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=198.66, default_y=-265.93):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=198.66, default_y=-230.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=198.66, default_y=-195.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=116.98, default_y=-551.98):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=116.98, default_y=-541.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-531.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-516.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-506.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-496.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-481.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-471.98):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=116.98, default_y=-461.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='15', width=220.36):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Staff(1)
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-405.93):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                        Accent()
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-390.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-380.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-355.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-335.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-320.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-310.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-300.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-285.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-275.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-250.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-230.93):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-205.93):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=23.09, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=87.57, default_y=-285.93):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=87.57, default_y=-250.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=87.57, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=87.57, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=110.84, default_y=-285.93):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=110.84, default_y=-250.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.84, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=110.84, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=135.69, default_y=-280.93):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=135.69, default_y=-245.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=135.69, default_y=-210.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=135.69, default_y=-175.93):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=160.55, default_y=-285.93):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=160.55, default_y=-250.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=160.55, default_y=-215.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=160.55, default_y=-180.93):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=187.89, default_y=-290.93):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=187.89, default_y=-255.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=187.89, default_y=-220.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=187.89, default_y=-185.93):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-80.0)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=110.84, default_y=-566.98):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=110.84, default_y=-526.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=110.84, default_y=-516.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=110.84, default_y=-496.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=110.84, default_y=-456.98):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=110.84, default_y=-446.98):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=110.84, default_y=-426.98):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='16', width=237.79):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(146.41)
                with StaffLayout(number=3):
                    StaffDistance(126.05)
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=62.31, default_y=-311.41):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                        Accent()
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-291.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-276.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-266.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-241.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-221.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-206.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-196.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-186.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-151.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-126.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-116.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-91.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note(default_x=62.31, default_y=-81.41):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=110.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=113.35, default_y=-171.41):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=113.35, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=113.35, default_y=-101.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=136.62, default_y=-171.41):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=136.62, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=136.62, default_y=-101.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=159.88, default_y=-161.41):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=159.88, default_y=-126.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=159.88, default_y=-91.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=183.15, default_y=-166.41):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=183.15, default_y=-131.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=183.15, default_y=-96.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=210.49, default_y=-171.41):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=210.49, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=210.49, default_y=-101.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-149.61)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=136.62, default_y=-447.46):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=136.62, default_y=-437.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-427.46):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-402.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-392.46):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-377.46):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-367.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-357.46):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-342.46):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-332.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=136.62, default_y=-322.46):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='17', width=208.56):
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=33.09, default_y=-306.41):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                        Accent()
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-296.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-281.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-261.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-236.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-226.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-211.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-191.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-176.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-156.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-121.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-106.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note(default_x=33.09, default_y=-86.41):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-30.09, default_y=105.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=84.13, default_y=-176.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=84.13, default_y=-141.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=84.13, default_y=-106.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=107.39, default_y=-176.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=107.39, default_y=-141.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=107.39, default_y=-106.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.66, default_y=-166.41):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=130.66, default_y=-131.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=130.66, default_y=-96.41):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=153.93, default_y=-171.41):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=153.93, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=153.93, default_y=-101.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=181.27, default_y=-176.41):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=181.27, default_y=-141.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=181.27, default_y=-106.41):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-149.61)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=107.39, default_y=-442.46):
                with Pitch():
                    Step('D')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=107.39, default_y=-432.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-407.46):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-397.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-372.46):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-362.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-337.46):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=107.39, default_y=-327.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='18', width=205.68):
            with Attributes():
                with Clef(number=3):
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=23.09, default_y=-311.41):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
                        Accent()
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-301.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-266.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-241.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-231.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-181.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-161.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-126.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-111.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note(default_x=23.09, default_y=-91.41):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Arpeggiate(default_x=-13.09, default_y=100.51)
            with Note():
                Rest()
                Duration(3.0)
                Voice('5')
                Type('16th')
                Dot()
                Staff(2)
            with Note(default_x=85.14, default_y=-181.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=85.14, default_y=-146.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=85.14, default_y=-111.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=85.14, default_y=-76.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('down')
                Staff(2)
            with Note(default_x=108.41, default_y=-181.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=108.41, default_y=-146.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=108.41, default_y=-111.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=108.41, default_y=-76.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=132.33, default_y=-171.41):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=132.33, default_y=-136.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=132.33, default_y=-101.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=132.33, default_y=-66.41):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(8)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.25, default_y=-176.41):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=156.25, default_y=-141.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.25, default_y=-106.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=156.25, default_y=-71.41):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=180.16, default_y=-181.41):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=180.16, default_y=-146.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=180.16, default_y=-111.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=180.16, default_y=-76.41):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('down')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-149.61)
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Note(default_x=108.41, default_y=-447.46):
                with Pitch():
                    Step('C')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=108.41, default_y=-437.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-412.46):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-402.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-377.46):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-367.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-342.46):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=108.41, default_y=-332.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                Rest()
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
        with Measure(number='19', width=227.55):
            with Direction(placement='below'):
                with DirectionType():
                    with Dynamics(default_x=3.29, default_y=-75.04, relative_y=-40.0):
                        Rf()
                Staff(1)
                Sound(dynamics=124.44)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=13.8, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=77.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('backward hook', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=77.7, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=77.7, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=77.7, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=102.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.28, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=102.28, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=126.86, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.86, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=126.86, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=163.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=163.22, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=163.22, default_y=60.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(7)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=198.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=198.49, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Note(default_x=198.49, default_y=50.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(6)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=102.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=158.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=158.92, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=158.92, default_y=35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(6)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=194.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=194.19, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=194.19, default_y=25.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(6)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(default_x=53.12, default_y=-457.46):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.99, default_y=-452.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(0)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=53.12, default_y=-422.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.99, default_y=-417.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=53.12, default_y=-387.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.99, default_y=-382.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=53.12, default_y=-352.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note(default_x=64.99, default_y=-347.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Stem('up')
                Staff(3)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('9')
                Type('eighth')
                Staff(3)
            with Note(default_x=158.92, default_y=-427.46):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(1)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=2)
            with Note(default_x=158.92, default_y=-417.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(1)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=158.92, default_y=-392.46):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=158.92, default_y=-382.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=158.92, default_y=-357.46):
                Chord()
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(3)
            with Note(default_x=158.92, default_y=-347.46):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.19, default_y=-437.46):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=194.19, default_y=-402.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.19, default_y=-367.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Note(default_x=194.19, default_y=-332.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('9')
                Type('16th')
                Stem('up')
                Staff(3)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-432.46):
                with Pitch():
                    Step('F')
                    Octave(1)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Articulations():
                        StrongAccent(type='down')
            with Note(default_x=13.8, default_y=-397.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=13.8, default_y=-362.46):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=102.28, default_y=-437.46):
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=102.28, default_y=-402.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
            with Note(default_x=102.28, default_y=-367.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('10')
                Type('quarter')
                Stem('down')
                Staff(3)
        with Measure(number='20', width=75.29):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=30.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=65.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=13.8, default_y=80.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=-85.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=43.74, default_y=-60.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=-50.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=20.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=45.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(6)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=55.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=43.74, default_y=80.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(7)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-457.46):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-437.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-422.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-387.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-367.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=13.8, default_y=-352.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='start', line='yes', default_y=-149.61)
                Staff(3)
            with Note(default_x=43.74, default_y=-457.46):
                with Pitch():
                    Step('A')
                    Octave(0)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
                with Notations():
                    with Articulations():
                        Staccatissimo()
            with Note(default_x=43.74, default_y=-422.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=43.74, default_y=-402.46):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
            with Note(default_x=43.74, default_y=-387.46):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('9')
                Type('quarter')
                Stem('up')
                Staff(3)
        with Measure(number='21', width=61.31):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('9')
                Staff(3)
        with Measure(number='22', width=61.31):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('9')
                Staff(3)
            with Direction(placement='below'):
                with DirectionType():
                    Pedal(type='stop', line='yes')
                Staff(3)
            with Barline(location='right'):
                BarStyle('light-heavy')