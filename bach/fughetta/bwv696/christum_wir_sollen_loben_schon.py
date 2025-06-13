with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle("Christum wir sollen loben schon oder: Was fürcht'st du, Feind Herodes, sehr. ")
    with Identification():
        Creator('Johann Sebastian Bach (1685-1750)', type='composer')
        Creator('BWV 696', type='lyricist')
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
        CreditWords('Christum wir sollen loben schon\n', default_x=595.44, default_y=1626.67, justify='center', valign='top', font_size='24')
        CreditWords("oder: Was fürcht'st du, Feind Herodes, sehr. \n")
        CreditWords(None)
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('Fughetta', default_x=595.44, default_y=1499.97, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685-1750)', default_x=1134.19, default_y=1436.67, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('BWV 696', default_x=56.6929, default_y=1436.67, justify='left', valign='bottom', font_size='12')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Orgel', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Orgel')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(23)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Orgel', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Orgel')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(12)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Orgel', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Orgel')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(116)
                Volume(78.7402)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=247.99):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    TopSystemDistance(260.0)
                with StaffLayout(number=2):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
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
                    with Metronome(parentheses='no', default_x=-37.67, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=83.68, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=156.19, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.29, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=226.95):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.28, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=129.57, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=161.5, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=193.43, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='3', width=259.29):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=75.87, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.82, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=192.75, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.94, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=43.4, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=75.87, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=160.29, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=192.75, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=225.22, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='4', width=322.27):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=90.52, default_y=-85.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=205.59, default_y=-105.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=243.95, default_y=-90.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.31, default_y=-95.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=52.16, default_y=-125.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=90.52, default_y=-110.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=128.87, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=167.23, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=205.59, default_y=-130.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=243.95, default_y=-115.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=282.31, default_y=-120.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='5', width=282.59):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.12)
                with StaffLayout(number=2):
                    StaffDistance(80.75)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=121.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=174.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=87.99, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=121.27, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=201.13, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=227.75, default_y=-105.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=254.37, default_y=-110.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-140.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=87.99, default_y=-135.75):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=104.63, default_y=-130.75):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=121.27, default_y=-125.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=147.89, default_y=-160.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=174.15, default_y=-140.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=237.15):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=72.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=155.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=182.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=208.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.52, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=46.1, default_y=-125.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=72.68, default_y=-110.75):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.25, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=125.83, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=155.73, default_y=-130.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.31, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=208.97, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-140.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='7', width=297.86):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=42.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=97.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=161.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-125.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=42.01, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=70.87, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=97.54, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=129.54, default_y=-125.75):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=161.55, default_y=-130.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=232.25, default_y=-125.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=264.26, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-140.75):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.54, default_y=-145.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=161.55, default_y=-145.75):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.55, default_y=-165.75):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=232.25, default_y=-150.75):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=264.26, default_y=-155.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='8', width=238.89):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=182.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=72.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=99.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=127.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=182.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=127.44, default_y=-115.75):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=154.91, default_y=-120.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=182.37, default_y=-105.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-160.75):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=99.98, default_y=-170.75):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=127.44, default_y=-155.75):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=154.91, default_y=-160.75):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=182.37, default_y=-165.75):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=209.83, default_y=-175.75):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='9', width=252.73):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.12)
                with StaffLayout(number=2):
                    StaffDistance(97.54)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=108.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=156.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=203.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=108.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=132.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=179.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=203.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=227.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-127.54):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=108.81, default_y=-112.54):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=132.53, default_y=-117.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.25, default_y=-122.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=179.97, default_y=-127.54):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=203.69, default_y=-132.54):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-172.54):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=108.45, default_y=-137.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=203.69, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=316.07):
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=94.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=197.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=253.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=64.34, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=94.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=125.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=156.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=197.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=283.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-127.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=64.34, default_y=-117.54):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=94.91, default_y=-137.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=156.06, default_y=-132.54):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=197.79, default_y=-127.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=224.46, default_y=-122.54):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=253.32, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=94.91, default_y=-147.54):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=125.49, default_y=-147.54):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=156.06, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=283.9, default_y=-147.54):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=248.69):
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=76.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=104.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=76.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=104.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=133.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=162.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=191.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=219.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=76.46, default_y=-137.54):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=191.31, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-152.54):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.82, default_y=-147.54):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=104.71, default_y=-152.54):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=133.57, default_y=-157.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=162.44, default_y=-167.54):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=191.31, default_y=-152.54):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=219.2, default_y=-157.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='12', width=239.0):
            with Note(default_x=16.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=185.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=43.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=69.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=100.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=132.15, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=185.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-142.54):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.62, default_y=-147.54):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=158.82, default_y=-167.54):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=185.01, default_y=-152.54):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.2, default_y=-157.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-162.54):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=69.62, default_y=-157.54):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.79, default_y=-177.54):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=279.83):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(0.0)
                    SystemDistance(95.12)
                with StaffLayout(number=2):
                    StaffDistance(89.09)
            with Note(default_x=73.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=131.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=198.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=232.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=255.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=73.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=109.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=131.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=232.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=73.77, default_y=-154.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=109.08, default_y=-144.09):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=131.54, default_y=-139.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=153.99, default_y=-134.09):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=176.09, default_y=-129.09):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=73.41, default_y=-164.09):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='14', width=229.53):
            with Note(default_x=14.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=38.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=72.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=156.42, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=180.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=204.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Direction(placement='below'):
                with DirectionType():
                    Words('(Pedal)', default_y=-62.15, relative_y=-35.0)
                Staff(2)
            with Note(default_x=14.16, default_y=-129.09):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=96.31, default_y=-149.09):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=132.58, default_y=-154.09):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=180.25, default_y=-139.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-184.09):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=132.58, default_y=-174.09):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.25, default_y=-174.09):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=274.35):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=50.5, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=80.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=111.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=141.98, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=177.29, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=211.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=242.25, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-139.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=80.99, default_y=-144.09):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=111.49, default_y=-149.09):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=141.98, default_y=-154.09):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=177.29, default_y=-149.09):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=211.76, default_y=-144.09):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.25, default_y=-139.09):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-169.09):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.99, default_y=-164.09):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=177.29, default_y=-184.09):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=211.76, default_y=-169.09):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=242.25, default_y=-174.09):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='16', width=272.79):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=158.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=41.49, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=75.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=99.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.66, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=243.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-134.09):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=130.74, default_y=-129.09):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=158.43, default_y=-149.09):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=215.8, default_y=-134.09):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-179.09):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=41.49, default_y=-184.09):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=99.23, default_y=-179.09):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=130.74, default_y=-174.09):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=158.43, default_y=-169.09):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=186.12, default_y=-164.09):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=215.8, default_y=-159.09):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=280.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(21.0)
                        RightMargin(-0.0)
                    SystemDistance(95.12)
                with StaffLayout(number=2):
                    StaffDistance(70.42)
            with Note(default_x=72.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=124.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=175.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=227.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=175.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-120.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=123.86, default_y=-120.42):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=227.52, default_y=-125.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=253.34, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=98.4, default_y=-145.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=124.22, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=150.05, default_y=-135.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=175.87, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=201.69, default_y=-150.42):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=227.52, default_y=-135.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=253.34, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
        with Measure(number='18', width=347.88):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=106.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Note(default_x=146.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Staff(1)
                Sound(tempo=72.0)
            with Note(default_x=185.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.07, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Note(default_x=146.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=185.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-135.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=56.07, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=146.07, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=186.3, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=226.29, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=266.29, default_y=-125.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=306.29, default_y=-130.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-145.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('begin', number=1)
            with Note(default_x=56.07, default_y=-155.42):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=106.07, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                Beam('continue', number=1)
            with Note(default_x=146.07, default_y=-145.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                Beam('end', number=1)
            with Note(default_x=185.94, default_y=-150.42):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                with DirectionType():
                    Words('.9', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-6.0)
                Staff(1)
                Sound(tempo=71.9)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                with DirectionType():
                    Words('.7', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-4.0)
                Staff(1)
                Sound(tempo=71.7)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('71')
                with DirectionType():
                    Words('.3', relative_y=20.0, font_weight='bold', font_size='12')
                Offset(-2.0)
                Staff(1)
                Sound(tempo=71.3)
        with Measure(number='19', width=307.48):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                with DirectionType():
                    Words('.6', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=70.6)
            with Note(default_x=19.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('64')
                with DirectionType():
                    Words('.5', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=64.5)
            with Note(default_x=163.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('62')
                Staff(1)
                Sound(tempo=62.0)
            with Note(default_x=198.75, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('59')
                with DirectionType():
                    Words('.1', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=59.1)
            with Note(default_x=234.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.03, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('55')
                with DirectionType():
                    Words('.8', default_y=13.03, relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=55.8)
            with Note(default_x=270.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
                Beam('end', number=1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.19, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('69')
                with DirectionType():
                    Words('.6', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=69.6)
            with Note(default_x=55.9, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('begin', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('68')
                with DirectionType():
                    Words('.2', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=68.2)
            with Note(default_x=91.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('continue', number=1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('66')
                with DirectionType():
                    Words('.5', relative_y=20.0, font_weight='bold', font_size='12')
                Staff(1)
                Sound(tempo=66.5)
            with Note(default_x=127.32, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                Beam('end', number=1)
            with Note(default_x=162.67, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.83, default_y=-135.42):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=162.67, default_y=-135.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.87, default_y=-145.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='20', width=120.37):
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_y=13.03, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('52')
                Staff(1)
                Sound(tempo=52.0)
            with Note(default_x=24.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-140.42):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-160.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-49.42, relative_y=-10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=247.99):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-145.0)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                Staves(2)
                with Clef(number=1):
                    Sign('G')
                    Line(2)
                with Clef(number=2):
                    Sign('F')
                    Line(4)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=83.68, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=156.19, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=201.29, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='2', width=226.95):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(16.0)
                Voice('5')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=67.28, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=129.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=161.5, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=193.43, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='3', width=259.29):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Staff(2)
            with Note(default_x=75.87, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=127.82, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=192.75, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.94, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=43.4, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=75.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=160.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=192.75, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=225.22, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='4', width=322.27):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('D')
                    DisplayOctave(5)
                Duration(16.0)
                Voice('2')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=90.52, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=205.59, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=243.95, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=282.31, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=52.16, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=90.52, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=128.87, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=167.23, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=205.59, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=243.95, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=282.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='5', width=282.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-160.75)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Staff(1)
            with Note(default_x=121.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=174.51, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=87.99, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=121.27, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=201.13, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=227.75, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=254.37, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=87.99, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=104.63, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('6')
                Type('16th')
                Stem('down')
                Staff(2)
            with Note(default_x=121.27, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=147.89, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=174.15, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='6', width=237.15):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=72.68, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
            with Note(default_x=155.73, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=182.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=208.97, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.52, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=46.1, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=72.68, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=99.25, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=125.83, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=155.73, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=182.31, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=208.97, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='7', width=297.86):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=42.01, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=97.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=161.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=42.01, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=70.87, default_y=5.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=97.54, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=129.54, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=161.55, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=232.25, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=264.26, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=10.0, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=97.54, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=161.55, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=193.55, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=232.25, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=264.26, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='8', width=238.89):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note(default_x=182.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=45.05, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=72.52, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=99.98, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.44, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=182.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=127.44, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=154.91, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=182.37, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.59, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=99.98, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=127.44, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=154.91, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
            with Note(default_x=182.37, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=209.83, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='9', width=252.73):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-177.54)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=61.37, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=108.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=156.25, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=203.69, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=108.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=132.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.25, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=179.97, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=203.69, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=227.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=108.81, default_y=25.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=132.53, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=156.25, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=179.97, default_y=10.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=203.69, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=61.37, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=108.45, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=203.69, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=316.07):
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=64.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=94.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=125.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=156.06, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=197.79, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=253.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=64.34, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=94.91, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=125.49, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=156.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=197.79, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=224.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=253.32, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=283.9, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=64.34, default_y=20.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=94.91, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=156.06, default_y=5.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=197.79, default_y=10.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=224.46, default_y=15.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('5')
                Type('16th')
                Stem('up')
                Staff(2)
            with Note(default_x=253.32, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=94.91, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=125.49, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=156.06, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=283.9, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(2)
        with Measure(number='11', width=248.69):
            with Note(default_x=21.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=76.82, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=104.71, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=133.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=76.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=104.71, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=133.57, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=162.44, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=191.31, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=219.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=76.46, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=191.31, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=21.03, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=76.82, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=104.71, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=133.57, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=162.44, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=191.31, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=219.2, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='12', width=239.0):
            with Note(default_x=16.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=185.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=43.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=69.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=100.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=132.15, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                Staff(1)
            with Note(default_x=185.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=69.62, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=158.82, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=185.01, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=211.2, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=69.62, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=131.79, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
        with Measure(number='13', width=279.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-169.09)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=73.77, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=131.54, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(1)
            with Note(default_x=198.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=232.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=255.06, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=73.77, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=109.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=131.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
                Staff(1)
            with Note(default_x=232.61, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=73.77, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=109.08, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=131.54, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=153.99, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=176.09, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=73.41, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note():
                Rest()
                Duration(8.0)
                Voice('6')
                Type('half')
                Staff(2)
        with Measure(number='14', width=229.53):
            with Note(default_x=14.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Staff(1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=38.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=72.47, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=156.42, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=180.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=204.09, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=14.16, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Staff(2)
            with Note(default_x=96.31, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=132.58, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=180.25, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Stem('down')
                Staff(2)
            with Note(default_x=132.58, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=180.25, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
        with Measure(number='15', width=274.35):
            with Note():
                with Rest(measure='yes'):
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(16.0)
                Voice('1')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=50.5, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=80.99, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=111.49, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=141.98, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=177.29, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Note(default_x=211.76, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=242.25, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=80.99, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Staff(2)
            with Note(default_x=111.49, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=141.98, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=177.29, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=211.76, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=242.25, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('6')
                Type('quarter')
                Stem('down')
                Staff(2)
            with Note(default_x=80.99, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('6')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(2)
            with Note(default_x=177.29, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=211.76, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=242.25, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='16', width=272.79):
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Staff(1)
            with Note(default_x=158.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=41.49, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=75.96, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=99.23, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.66, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=243.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('5')
                Type('quarter')
                Dot()
                Stem('up')
                Staff(2)
            with Note(default_x=130.74, default_y=0.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=158.43, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=215.8, default_y=-5.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=41.49, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=99.23, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=130.74, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=158.43, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=186.12, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=215.8, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('6')
                Type('quarter')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=280.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-150.42)
                with StaffLayout(number=2):
                    StaffDistance(0.0)
            with Note(default_x=72.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=124.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=175.87, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
            with Note(default_x=227.52, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=124.22, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=175.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
            with Note(default_x=227.52, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=123.86, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Stem('up')
                Staff(2)
            with Note(default_x=227.52, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=253.34, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=72.58, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=98.4, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=124.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=150.05, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=175.87, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=201.69, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=227.52, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=253.34, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
        with Measure(number='18', width=347.88):
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=106.07, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=146.07, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(1)
            with Note(default_x=185.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=56.07, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Staff(1)
            with Note(default_x=81.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Staff(1)
            with Note(default_x=106.07, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=146.07, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=185.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Accidental('natural')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=56.07, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('5')
                Type('quarter')
                Stem('up')
                Staff(2)
            with Note(default_x=146.07, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='start')
            with Note(default_x=186.3, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=226.29, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Note(default_x=266.29, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Note(default_x=306.29, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('5')
                Type('eighth')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=56.07, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Staff(2)
            with Note(default_x=106.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Staff(2)
            with Note(default_x=146.07, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('6')
                Type('eighth')
                Stem('down')
                Staff(2)
            with Note(default_x=185.94, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('6')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(2)
        with Measure(number='19', width=307.48):
            with Note(default_x=19.83, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=163.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=198.75, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=234.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Staff(1)
            with Note(default_x=270.17, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=20.19, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.9, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=91.61, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=127.32, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Staff(1)
            with Note(default_x=162.67, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('half')
                Accidental('sharp')
                Stem('down')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=19.83, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('sharp')
                Stem('up')
                Staff(2)
            with Note(default_x=162.67, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('5')
                Type('half')
                Accidental('natural')
                Stem('up')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('6')
                Type('whole')
                Staff(2)
        with Measure(number='20', width=120.37):
            with Note(default_x=24.35, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Staff(1)
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('2')
                Type('whole')
                Accidental('sharp')
                Staff(1)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(16.0)
                Voice('5')
                Type('whole')
                Staff(2)
            with Backup():
                Duration(16.0)
            with Note(default_x=24.35, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('6')
                Type('whole')
                Staff(2)
                with Notations():
                    Fermata(None, type='inverted', default_y=-49.42, relative_y=-10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=247.99):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='2', width=226.95):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='3', width=259.29):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='4', width=322.27):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='5', width=282.59):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='6', width=237.15):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='7', width=297.86):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='8', width=238.89):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='9', width=252.73):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='10', width=316.07):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='11', width=248.69):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='12', width=239.0):
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='13', width=279.83):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('1')
        with Measure(number='14', width=229.53):
            with Note(default_x=13.8, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=132.58, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=180.25, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='15', width=274.35):
            with Note(default_x=20.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=80.99, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=177.29, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=211.76, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=242.25, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='16', width=272.79):
            with Note(default_x=13.8, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=41.49, default_y=-55.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=99.23, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=130.74, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=158.43, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=186.12, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=215.8, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=280.76):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=72.58, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=98.4, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.22, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.05, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=175.87, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=201.69, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=227.52, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=253.34, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='18', width=347.88):
            with Note(default_x=13.8, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=56.07, default_y=-45.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=106.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=146.07, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=185.94, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('sharp')
                Stem('up')
        with Measure(number='19', width=307.48):
            with Note(default_x=16.87, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='20', width=120.37):
            with Note(default_x=24.35, default_y=-50.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')