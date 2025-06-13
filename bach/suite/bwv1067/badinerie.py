with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('BADINERIE (Guitar)')
    with Identification():
        Creator('C.Cochener/P.Bucky', type='arranger')
        Creator('Jean Sébastien Bach', type='composer')
        Rights('Cochener')
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
        CreditWords('BADINERIE (Guitar)\n', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
        CreditWords(' \n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('J-S Bach', default_x=595.44, default_y=1569.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Cochener', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Cochener', default_x=595.44, default_y=113.386, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('none')
        with ScorePart(id='P1'):
            PartName('Guitare électrique')
            PartAbbreviation('Guit. El.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Guitare électrique')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(28)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=249.9):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(170.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(2)
                with Time():
                    Beats('2')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
                with Clef(number=2):
                    Sign('TAB')
                    Line(5)
                with StaffDetails(number=2):
                    StaffLines(6)
                    with StaffTuning(line=1):
                        TuningStep('E')
                        TuningOctave(2)
                    with StaffTuning(line=2):
                        TuningStep('A')
                        TuningOctave(2)
                    with StaffTuning(line=3):
                        TuningStep('D')
                        TuningOctave(3)
                    with StaffTuning(line=4):
                        TuningStep('G')
                        TuningOctave(3)
                    with StaffTuning(line=5):
                        TuningStep('B')
                        TuningOctave(3)
                    with StaffTuning(line=6):
                        TuningStep('E')
                        TuningOctave(4)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-36.0, default_y=18.22, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('120')
                Staff(1)
                Sound(tempo=120.0)
            with Note(default_x=109.1, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=137.36, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.63, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=178.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=206.55, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=111.59, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=134.85, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=163.12, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=180.79, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=209.05, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=226.71, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
        with Measure(number='2', width=102.54):
            with Note(default_x=12.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=70.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=37.74, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=55.24, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=72.74, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
        with Measure(number='3', width=179.54):
            with Note(default_x=12.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.59, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=133.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=153.85, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-150.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(4)
            with Note(default_x=35.55, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(4)
            with Note(default_x=55.68, default_y=-120.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(3)
            with Note(default_x=75.81, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(4)
            with Note(default_x=95.95, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(2)
            with Note(default_x=116.08, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(4)
            with Note(default_x=136.22, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(2)
            with Note(default_x=156.35, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(4)
        with Measure(number='4', width=145.35):
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.95, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=87.52, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=115.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.73, default_y=-135.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(3)
            with Note(default_x=37.3, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(2)
            with Note(default_x=54.87, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=72.44, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(2)
            with Note(default_x=90.02, default_y=-120.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(3)
            with Note(default_x=118.13, default_y=-135.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(4)
        with Measure(number='5', width=156.6):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=44.06, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=67.33, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=84.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=113.26, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.3, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=41.56, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=69.83, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=87.49, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=115.75, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=133.42, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
        with Measure(number='6', width=102.54):
            with Note(default_x=12.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.74, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=70.24, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=37.74, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=55.24, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=72.74, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
        with Measure(number='7', width=141.04):
            with Note(default_x=12.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=30.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=48.06, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=76.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=93.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=111.32, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=32.99, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=50.56, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=78.67, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=96.25, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=113.82, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
        with Measure(number='8', width=243.29):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(93.32)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=91.84, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=123.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=154.77, default_y=-10.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('forward hook', number=2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=165.74, default_y=-5.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=177.46, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=209.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=94.34, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=126.45, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=149.18, default_y=-135.0):
                Grace()
                with Pitch():
                    Step('D')
                    Octave(4)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=165.93, default_y=-135.0):
                Grace(slash='yes')
                with Pitch():
                    Step('E')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=179.95, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=207.07, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(11)
        with Measure(number='9', width=174.14):
            with Note(default_x=12.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=63.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=139.07, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=45.31, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(6)
            with Note(default_x=66.24, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=99.71, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=120.64, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(6)
            with Note(default_x=141.56, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
        with Measure(number='10', width=185.66):
            with Note(default_x=15.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=54.05, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=84.87, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.84, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=145.81, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.29, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=56.55, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=79.28, default_y=-120.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=96.03, default_y=-120.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=110.05, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=143.3, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
        with Measure(number='11', width=228.02):
            with Note(default_x=14.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.01, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=147.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=173.16, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.91, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(11)
            with Note(default_x=37.75, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=63.5, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=89.25, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=124.15, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=144.9, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=175.66, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=196.41, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
        with Measure(number='12', width=246.38):
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.13, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.82, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=134.02, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=161.71, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=189.4, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.09, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.73, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
            with Note(default_x=49.63, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=72.31, default_y=-120.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(12)
            with Note(default_x=108.82, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=131.51, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=164.21, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=186.89, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=219.59, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
        with Measure(number='13', width=312.1):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(93.32)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.04, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=115.07, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=199.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.07, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=283.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=85.53, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=112.57, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=139.6, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=169.5, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
            with Note(default_x=196.53, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=223.56, default_y=-120.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(12)
            with Note(default_x=250.59, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=280.49, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
        with Measure(number='14', width=235.81):
            with Note(default_x=14.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.99, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.47, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.85, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.33, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.81, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=43.48, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(9)
            with Note(default_x=64.96, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=94.86, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
            with Note(default_x=121.34, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=147.82, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=174.3, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=204.2, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(10)
        with Measure(number='15', width=237.28):
            with Note(default_x=14.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.53, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=68.56, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.58, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.61, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=149.64, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=208.17, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=39.03, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=71.06, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(9)
            with Note(default_x=93.08, default_y=-120.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(12)
            with Note(default_x=125.11, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(9)
            with Note(default_x=147.13, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=183.64, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=205.66, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
        with Measure(number='16', width=129.96):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=47.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=72.42, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.29, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=49.8, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Ornaments():
                        TrillMark()
                    with Technical():
                        String(2)
                        Fret(9)
            with Note(default_x=69.91, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='17', width=162.35):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=24.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=53.35, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=71.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=89.57, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=118.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=26.86, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=55.84, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(5)
            with Note(default_x=73.96, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=92.07, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=121.05, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=139.16, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
        with Measure(number='18', width=176.09):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(93.32)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=144.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=90.54, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(7)
            with Note(default_x=112.2, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=129.7, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(7)
            with Note(default_x=147.2, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(5)
                        Fret(9)
        with Measure(number='19', width=142.48):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=39.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.96, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=95.86, default_y=-10.0):
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
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=11.49, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(10)
            with Note(default_x=42.48, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Note(default_x=68.46, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=98.36, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(8)
            with Note(default_x=110.86, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
        with Measure(number='20', width=129.62):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.7, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=57.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=78.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=103.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.29, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=43.2, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=54.78, default_y=-135.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(11)
            with Note(default_x=80.71, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=105.61, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='21', width=143.79):
            with Note(default_x=12.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.28, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=57.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=75.24, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=100.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=40.78, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=60.24, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=77.74, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=103.1, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=120.6, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='22', width=122.16):
            with Note(default_x=14.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=54.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    with Articulations():
                        Falloff()
            with Note(default_x=87.76, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(11)
            with Note(default_x=40.86, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=52.44, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Articulations():
                        Falloff()
                    with Technical():
                        String(4)
                        Fret(11)
            with Note(default_x=90.25, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        String(4)
                        Fret(7)
        with Measure(number='23', width=185.4):
            with Note(default_x=15.5, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=37.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.8, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=98.56, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=118.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=159.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    with Technical():
                        String(4)
                        Fret(7)
            with Note(default_x=39.91, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=60.29, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=80.68, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=101.06, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=121.45, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=141.83, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=162.21, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
        with Measure(number='24', width=177.96):
            with Note(default_x=12.92, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.74, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.64, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=92.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=112.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.37, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=152.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=35.32, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=55.23, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=75.14, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=95.05, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=114.96, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=134.87, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=154.78, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
        with Measure(number='25', width=267.99):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(93.32)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.08, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.16, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=176.19, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=198.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=90.54, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=112.58, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=134.61, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=156.65, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=178.69, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=200.73, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=222.77, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=244.8, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
        with Measure(number='26', width=192.87):
            with Note(default_x=12.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.96, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=56.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.03, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=101.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.11, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=145.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=167.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=37.45, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(5)
            with Note(default_x=59.49, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=81.53, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=103.57, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=125.61, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=147.64, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=169.68, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
        with Measure(number='27', width=203.53):
            with Note(default_x=12.92, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.04, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=107.17, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=130.73, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.85, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=38.98, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=62.54, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(5)
            with Note(default_x=86.1, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=109.66, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(5)
            with Note(default_x=133.22, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=156.79, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=180.35, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
        with Measure(number='28', width=96.62):
            with Note(default_x=12.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=35.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=58.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=38.22, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Ornaments():
                        TrillMark()
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=61.03, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
        with Measure(number='29', width=154.37):
            with Note(default_x=12.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=51.76, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=82.84, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.27, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=121.69, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=34.84, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=54.26, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=85.34, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=104.76, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=124.19, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
        with Measure(number='30', width=162.12):
            with Note(default_x=15.8, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=77.02, default_y=0.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=87.99, default_y=5.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('1')
                Type('16th')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=130.11, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.29, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=48.7, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=71.43, default_y=-120.0):
                Grace()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=88.18, default_y=-120.0):
                Grace()
                with Pitch():
                    Step('G')
                    Octave(4)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=102.2, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=132.61, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='31', width=227.7):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=107.22, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=126.39, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=157.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=176.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=195.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=90.54, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=109.71, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=128.89, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=159.57, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=178.74, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=197.92, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='32', width=116.96):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=40.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=65.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=90.47, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=18.3, default_y=-105.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(9)
            with Note(default_x=43.19, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=68.08, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(5)
            with Note(default_x=92.97, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
        with Measure(number='33', width=156.27):
            with Note(default_x=15.8, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=46.91, default_y=25.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.18, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.45, default_y=10.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=111.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=18.3, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=44.41, default_y=-105.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(10)
            with Note(default_x=72.68, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=94.46, default_y=-120.0):
                Grace()
                with Pitch():
                    Step('A')
                    Octave(4)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=114.39, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        String(2)
                        Fret(8)
        with Measure(number='34', width=170.12):
            with Note(default_x=15.5, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.98, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=71.25, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=92.17, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=109.67, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=127.17, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=50.48, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=68.74, default_y=-120.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        String(2)
                        Fret(10)
            with Note(default_x=94.67, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=112.17, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=129.67, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='start')
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='35', width=231.61):
            with Note(default_x=15.5, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=50.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.62, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=102.62, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=129.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=154.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=179.65, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=204.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=52.62, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=70.12, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=87.62, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=105.12, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    Slur(type='stop', number=1)
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=126.78, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(10)
            with Note(default_x=156.96, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=182.14, default_y=-120.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(8)
            with Note(default_x=207.32, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='36', width=174.84):
            with Note(default_x=14.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=34.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.68, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=139.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=11.49, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(10)
            with Note(default_x=37.42, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Note(default_x=53.25, default_y=-150.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(10)
            with Note(default_x=79.18, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Note(default_x=109.07, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(8)
            with Note(default_x=142.4, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(5)
                        Fret(9)
        with Measure(number='37', width=320.39):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Note(default_x=88.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=142.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=196.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=250.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=284.86, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(16.0)
            with Note(default_x=85.53, default_y=-165.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(5)
                        Fret(10)
            with Note(default_x=144.83, default_y=-165.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(5)
                        Fret(9)
            with Note(default_x=199.12, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Note(default_x=253.42, default_y=-150.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(8)
            with Note(default_x=287.35, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
        with Measure(number='38', width=285.61):
            with Note(default_x=12.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=64.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=101.47, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=138.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=190.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=213.32, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=236.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
                Beam('continue', number=3)
            with Note(default_x=259.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=66.68, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=103.97, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=141.25, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=192.52, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Note(default_x=215.82, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=239.12, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=262.43, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('32nd')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
        with Measure(number='39', width=227.86):
            with Note(default_x=12.92, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=63.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=94.49, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.86, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=176.06, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=65.61, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=96.99, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
            with Note(default_x=128.36, default_y=-105.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(1)
                        Fret(7)
            with Note(default_x=178.56, default_y=-120.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('eighth')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(2)
                        Fret(7)
        with Measure(number='40', width=243.63):
            with Note(default_x=12.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=116.15, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=150.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=15.41, default_y=-135.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(9)
            with Note(default_x=49.82, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=84.24, default_y=-135.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(6)
            with Note(default_x=118.65, default_y=-135.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('16th')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(3)
                        Fret(7)
            with Note(default_x=153.06, default_y=-150.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('quarter')
                Stem('none')
                Staff(2)
                with Notations():
                    with Technical():
                        String(4)
                        Fret(9)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')