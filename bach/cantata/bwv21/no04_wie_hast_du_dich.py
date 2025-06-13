with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 21')
        WorkTitle('Ich hatte viel bekümmernis')
    MovementNumber('BWV 21 #4 (in Part One)')
    MovementTitle('Wie, hast du dich')
    with Identification():
        Creator('Edward J. Maurath', type='arranger')
        Creator('Johann Sebastian Bach (1685--1750)', type='composer')
        Creator('Solomon Franck', type='lyricist')
        Creator('Baroque Church Cantata', type='poet')
        Rights('Sequenced by Edward J. Maurath')
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
            PageHeight(1583.9)
            PageWidth(1223.92)
            with PageMargins(type='both'):
                LeftMargin(56.6893)
                RightMargin(56.6893)
                TopMargin(56.6893)
                BottomMargin(113.379)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('\n', default_x=611.961, default_y=1519.38, justify='center', valign='top', font_size='24')
        CreditWords('BWV 21 #04 Wie, hast du dich')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('\n', default_x=611.961, default_y=1464.56, justify='center', valign='top', font_size='14')
        CreditWords('Tenor recitative in c minor\n')
        CreditWords('\n')
        CreditWords('Sequenced by Edward J. Maurath\n')
        CreditWords('More at bach.ejmaurath.com')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685--1750)\n', default_x=1167.23, default_y=1054.43, justify='right', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('lyricist')
        CreditWords('Solomon Franck\n', default_x=56.6893, default_y=1054.43, justify='left', valign='bottom', font_size='12')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords('\n')
        CreditWords(None)
    with Credit(page=1):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('Sequenced by Edward J. Maurath', default_x=611.961, default_y=113.379, justify='center', valign='bottom', font_size='8')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Violin\n1')
            PartAbbreviation('VN1')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(41)
                Volume(49.6063)
                Pan(-30.0)
        with ScorePart(id='P2'):
            PartName('Violin\n2')
            PartAbbreviation('VN2')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(41)
                Volume(48.8189)
                Pan(-37.0)
        PartGroup(type='stop', number='1')
        with ScorePart(id='P3'):
            PartName('Viola')
            PartAbbreviation('VLA')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Flute')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(42)
                Volume(48.0315)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Tenore')
            PartAbbreviation('TEN')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(58)
                Volume(69.2913)
                Pan(37.0)
        with PartGroup(type='start', number='1'):
            GroupSymbol('brace')
        with ScorePart(id='P5'):
            PartName('Organo\nContinuo')
            PartAbbreviation('ORG')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Organ')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(75)
                Volume(48.0315)
                Pan(-90.0)
        with ScorePart(id='P6'):
            PartName('Bassoon\nContinuo')
            PartAbbreviation('BSN\nB.C.')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(71)
                Volume(48.8189)
                Pan(90.0)
        PartGroup(type='stop', number='1')
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P7'):
            PartName('Violoncelli\nContinuo')
            PartAbbreviation('VCI\nB.C.')
            with ScoreInstrument(id='P7-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P7-I1', port=1)
            with MidiInstrument(id='P7-I1'):
                MidiChannel(7)
                MidiProgram(49)
                Volume(48.8189)
                Pan(0.0)
        with ScorePart(id='P8'):
            PartName('Contrabassi\nContinuo')
            PartAbbreviation('CBI\nB.C.')
            with ScoreInstrument(id='P8-I1'):
                InstrumentName('Bassoon')
            MidiDevice(None, id='P8-I1', port=1)
            with MidiInstrument(id='P8-I1'):
                MidiChannel(8)
                MidiProgram(49)
                Volume(49.6063)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=286.39):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(120.59)
                        RightMargin(-0.0)
                    TopSystemDistance(542.78)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    Words('60', default_x=-39.32, relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=60.0)
            with Note(default_x=113.73, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=182.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='2', width=223.35):
            with Note(default_x=18.64, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=77.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=15.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(65.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=101.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
        with Measure(number='6', width=194.55):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('down')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=126.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.81, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.38, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=151.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', default_y=4.42, relative_y=10.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(65.0)
                        RightMargin(-0.0)
                    SystemDistance(353.83)
            with Note(default_x=89.72, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=15.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.4, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.06, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=246.66):
            with Note(default_x=20.36, default_y=10.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
            with Note(default_x=131.53, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(65.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=100.92, default_y=15.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.76, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=205.95, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Direction(placement='above'):
                with DirectionType():
                    Words('48', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=48.0)
            with Note(default_x=127.02, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=12.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='17', width=197.1):
            with Direction(placement='above'):
                with DirectionType():
                    Words('36', relative_y=20.0, font_weight='bold', font_size='12')
                Sound(tempo=36.0)
            with Note(default_x=16.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=63.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=92.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=113.73, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.51, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='2', width=223.35):
            with Note(default_x=18.28, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=132.62, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=16.2, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.43, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.07, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=101.76, default_y=-145.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
        with Measure(number='6', width=194.55):
            with Note(default_x=17.23, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.39, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.72, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=73.54, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.0, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=151.83, default_y=-140.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=177.62, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.48, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-150.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=89.72, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=16.2, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.27, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=132.33, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.4, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=223.06, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.73, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=246.66):
            with Note(default_x=17.4, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='13', width=224.07):
            with Note(default_x=15.84, default_y=-105.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=116.86, default_y=-115.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.56, default_y=-110.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=205.95, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=127.38, default_y=-125.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.26, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=300.68):
            with Note(default_x=15.84, default_y=-130.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('up')
            with Note(default_x=220.56, default_y=-135.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='17', width=197.1):
            with Note(default_x=12.88, default_y=-120.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('C')
                    Line(3)
            with Note(default_x=113.73, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=182.51, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='2', width=223.35):
            with Note(default_x=15.32, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=15.84, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=101.76, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='6', width=194.55):
            with Note(default_x=17.23, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=51.39, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=-215.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=126.36, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.23, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=181.64, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.05, default_y=-215.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=47.81, default_y=-225.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=99.02, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-235.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=89.72, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=15.84, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=132.33, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('flat')
                Stem('down')
            with Note(default_x=223.06, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.73, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=246.66):
            with Note(default_x=17.4, default_y=-195.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.92, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=147.76, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=205.95, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.02, default_y=-220.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=15.84, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=152.44, default_y=-230.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.5, default_y=-200.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=220.56, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=254.62, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='17', width=197.1):
            with Note(default_x=16.2, default_y=-205.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=63.46, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=92.99, default_y=-215.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.16, default_y=-210.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                with Transpose():
                    Diatonic(0)
                    Chromatic(0.0)
                    OctaveChange(-1)
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=156.36, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=182.87, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=215.2, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=231.77, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=258.28, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=223.35):
            with Note(default_x=18.64, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=61.38, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
            with Note(default_x=77.82, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=104.12, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=132.98, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=195.45, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='3', width=275.32):
            with Note(default_x=16.2, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.82, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=77.43, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=114.77, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=141.43, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.57, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=179.71, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=240.94, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.72, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.44, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=71.34, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=106.36, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=124.31, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=105.08, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
            with Note(default_x=169.12, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=184.78, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.45, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=222.01, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=194.55):
            with Note(default_x=17.23, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=51.75, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=111.37, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=127.06, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.75, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.85, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='7', width=236.06):
            with Note(default_x=20.72, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.13, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=99.95, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=126.36, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=155.23, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=181.64, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=208.05, default_y=-360.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-355.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=73.6, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=99.38, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.17, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=151.83, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=206.48, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=112.14, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=93.04, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=120.24, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=147.44, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=184.34, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=201.34, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=265.94, default_y=-355.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
        with Measure(number='11', width=274.49):
            with Note(default_x=16.2, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.23, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=74.27, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.3, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=132.33, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=161.36, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='12', width=246.66):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=49.02, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=77.31, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=114.21, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=131.89, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.18, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.48, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=216.77, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=224.07):
            with Note(default_x=16.2, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=41.46, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=91.97, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=117.22, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=167.74, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=183.52, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.31, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(65.0)
            with Note(default_x=100.92, default_y=-310.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=177.04, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=206.31, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=282.43, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.72, default_y=-320.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=88.91, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=127.38, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=203.57, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=16.2, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=50.26, default_y=-340.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=84.32, default_y=-345.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=118.38, default_y=-350.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=152.44, default_y=-315.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=186.5, default_y=-325.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=220.56, default_y=-335.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=275.91, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('backward hook', number=2)
        with Measure(number='17', width=197.1):
            with Note(default_x=16.2, default_y=-330.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('half')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P5'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-355.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=113.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.73, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=113.73, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.51, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.51, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=182.51, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
        with Measure(number='2', width=223.35):
            with Note(default_x=21.24, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=132.62, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=77.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(16.0)
                Tie(type='start')
                Voice('3')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=77.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=141.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('3')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(8.0)
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=124.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Forward():
                Duration(4.0)
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-355.0)
            with Note(default_x=101.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('natural')
            with Backup():
                Duration(16.0)
            with Note(default_x=101.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('3')
                Type('whole')
        with Measure(number='6', width=194.55):
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.39, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=51.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(12.0)
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=51.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('up')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=130.66, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(8.0)
            with Note(default_x=126.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=20.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('half')
                Stem('up')
            with Note(default_x=131.39, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=155.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=181.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=208.05, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.81, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.75, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=151.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(12.0)
                Tie(type='stop')
                Voice('2')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=151.83, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=177.62, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
            with Note(default_x=206.48, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(4.0)
            with Note(default_x=99.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('half')
                Stem('up')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=5.9, relative_y=10.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=67.78, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('2')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=14.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=67.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('3')
                Type('half')
                Accidental('flat')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-355.0)
            with Note(default_x=89.72, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=89.72, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('2')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=89.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('3')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=20.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=132.33, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=132.33, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=190.4, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=190.4, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=190.4, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
            with Note(default_x=223.06, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=223.06, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=223.06, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=249.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
            with Note(default_x=249.73, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Note(default_x=249.73, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.27, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Backup():
                Duration(8.0)
            with Note(default_x=15.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('3')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Forward():
                Duration(8.0)
        with Measure(number='12', width=246.66):
            with Note(default_x=23.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
            with Note(default_x=131.53, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('2')
                Type('whole')
            with Backup():
                Duration(16.0)
            with Note(default_x=17.4, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('3')
                Type('whole')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=116.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-355.0)
            with Note(default_x=100.92, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=147.76, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
            with Note(default_x=205.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(16.0)
            with Note(default_x=100.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=205.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('up')
            with Backup():
                Duration(16.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=147.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=205.95, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='start')
                Voice('3')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('up')
            with Note(default_x=127.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=174.26, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note(default_x=12.36, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Tie(type='stop')
                Voice('3')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=127.02, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=20.5, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(16.0)
            with Note(default_x=15.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(12.0)
                Voice('2')
                Type('half')
                Dot()
                Accidental('flat')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=26.42, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(8.0)
                Tie(type='start')
                Voice('3')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=152.44, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=152.44, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=152.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.5, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('flat')
                Stem('up')
            with Note(default_x=186.5, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=186.5, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=220.56, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=220.56, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=232.43, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('up')
        with Measure(number='17', width=197.1):
            with Note(default_x=12.88, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Backup():
                Duration(16.0)
            with Note(default_x=16.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=16.2, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('flat')
                Stem('down')
            with Note(default_x=63.46, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
            with Note(default_x=63.46, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=92.99, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=92.99, default_y=-35.0):
                Chord()
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=122.16, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Note(default_x=122.16, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('2')
                Type('half')
                Stem('down')
            with Backup():
                Duration(16.0)
            with Note():
                Rest(measure='yes')
                Duration(16.0)
                Voice('3')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P6'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=110.77, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=223.35):
            with Note(default_x=15.32, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=15.84, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=101.76, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='6', width=194.55):
            with Note(default_x=13.91, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=126.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.81, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.02, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=89.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.27, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=131.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=246.66):
            with Note(default_x=17.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note(default_x=97.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=127.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=15.84, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=152.08, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='17', width=197.1):
            with Note(default_x=12.88, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P7'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(420.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=110.77, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=223.35):
            with Note(default_x=15.32, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=15.84, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(420.0)
            with Note(default_x=101.76, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='6', width=194.55):
            with Note(default_x=13.91, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=-440.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=126.0, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.81, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.02, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-460.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(420.0)
            with Note(default_x=89.72, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=16.2, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.27, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=131.97, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=246.66):
            with Note(default_x=17.4, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=-450.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(420.0)
            with Note(default_x=97.6, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-455.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=127.02, default_y=-435.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=15.84, default_y=-430.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=152.08, default_y=-440.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='17', width=197.1):
            with Note(default_x=12.88, default_y=-445.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P8'):
        with Measure(number='1', width=286.39):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-460.0)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-2)
                with Time():
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
                    ClefOctaveChange(-1)
            with Note(default_x=110.77, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='start')
        with Measure(number='2', width=223.35):
            with Note(default_x=15.32, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='3', width=275.32):
            with Note(default_x=15.84, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=141.07, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='4', width=204.89):
            with Note(default_x=12.36, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=124.31, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
        with Measure(number='5', width=246.78):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-460.0)
            with Note(default_x=101.76, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
                Accidental('sharp')
        with Measure(number='6', width=194.55):
            with Note(default_x=13.91, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='7', width=236.06):
            with Note(default_x=20.36, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=126.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
        with Measure(number='8', width=231.25):
            with Note(default_x=12.36, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=47.81, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=99.02, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('up')
        with Measure(number='9', width=136.9):
            with Note(default_x=14.0, default_y=-40.0):
                with Pitch():
                    Step('G')
                    Octave(1)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=67.78, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='10', width=300.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-460.0)
            with Note(default_x=89.72, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
        with Measure(number='11', width=274.49):
            with Note(default_x=16.2, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=74.27, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note(default_x=131.97, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='12', width=246.66):
            with Note(default_x=17.4, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(16.0)
                Tie(type='stop')
                Voice('1')
                Type('whole')
                with Notations():
                    Tied(type='stop')
        with Measure(number='13', width=224.07):
            with Note(default_x=12.88, default_y=-30.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(1)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='14', width=313.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-460.0)
            with Note(default_x=97.6, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
        with Measure(number='15', width=234.47):
            with Note(default_x=12.36, default_y=-35.0):
                with Pitch():
                    Step('A')
                    Octave(1)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Note(default_x=127.02, default_y=-15.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('natural')
                Stem('down')
        with Measure(number='16', width=300.68):
            with Note(default_x=15.84, default_y=-10.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('down')
            with Note(default_x=152.08, default_y=-20.0):
                with Pitch():
                    Step('D')
                    Alter(-1.0)
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Accidental('flat')
                Stem('down')
        with Measure(number='17', width=197.1):
            with Note(default_x=12.88, default_y=-25.0):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(16.0)
                Voice('1')
                Type('whole')
            with Barline(location='right'):
                BarStyle('light-heavy')