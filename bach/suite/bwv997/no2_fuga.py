with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 997')
    with Identification():
        Creator('Johann Sebastian Bach', type='composer')
        Rights('by Mutopia 2013/02/17-51\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ')
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
            Millimeters(6.256)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1898.98)
            PageWidth(1342.71)
            with PageMargins(type='even'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(127.877)
            with PageMargins(type='odd'):
                LeftMargin(63.9386)
                RightMargin(63.9386)
                TopMargin(63.9386)
                BottomMargin(127.877)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='FreeSerif', font_size='11')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Suite in C Minor for Lute (trans. to A minor)', default_x=671.355, default_y=1835.04, justify='center', valign='top', font_family='Times New Roman', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('2. Fuga', default_x=671.355, default_y=1771.1, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685-1750)\n', default_x=1278.77, default_y=1711.2, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
        CreditWords('BWV 997')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('by Mutopia 2013/02/17-51\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ', default_x=671.355, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=2):
        CreditType('rights')
        CreditWords('by Mutopia 2013/02/17-51\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ', default_x=671.355, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with Credit(page=3):
        CreditType('rights')
        CreditWords('by Mutopia 2013/02/17-51\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ', default_x=671.355, default_y=127.877, justify='center', valign='bottom', font_size='8')
    with PartList():
        with ScorePart(id='P1'):
            PartName('Chitarra', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Chitarra')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(25)
                Volume(83.4646)
                Pan(0.0)
    with Part(id='P1'):
        with Measure(number='1', width=244.35):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(212.79)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('6')
                    BeatType('8')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-35.06, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('100')
                Sound(tempo=100.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=103.17, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=131.09, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=159.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=186.92, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=214.83, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                Rest()
                Duration(12.0)
                Voice('2')
                Type('half')
                Dot()
        with Measure(number='2', width=223.08):
            with Direction(placement='above'):
                with DirectionType():
                    Segno(default_x=-8.12, relative_y=20.0)
                Sound(segno='segno')
            with Note(default_x=12.12, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=116.8, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=47.01, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=81.91, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=116.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.69, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=186.59, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='3', width=226.76):
            with Note(default_x=15.8, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=120.48, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.69, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=85.59, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=120.48, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.37, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=190.27, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='4', width=253.92):
            with Note(default_x=15.8, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=51.63, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=87.45, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=123.28, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=162.71, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=194.1, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=216.5, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=123.28, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='5', width=266.73):
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=130.63, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=226.85, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.08, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.35, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=142.5, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=171.53, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=202.93, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=226.85, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='6', width=307.13):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=55.2, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=191.56, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=223.14, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=242.88, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.62, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.36, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=76.1, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=128.39, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=159.97, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=191.56, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
        with Measure(number='7', width=249.99):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=45.1, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=78.07, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=129.01, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=182.43, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=215.41, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('up')
            with Note(default_x=89.07, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
            with Note(default_x=136.01, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=129.01, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.43, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=215.41, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='8', width=192.49):
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=41.87, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.93, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=99.33, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=103.33, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=138.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=164.82, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=164.82, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='9', width=195.87):
            with Note(default_x=20.23, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=113.75, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=24.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.43, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=76.09, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=119.75, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=166.61, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=166.61, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='10', width=269.36):
            with Note(default_x=12.0, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.2, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=90.23, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=123.26, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=182.69, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=214.08, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=234.73, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=133.26, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.23, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
            with Note(default_x=123.26, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=234.73, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='11', width=305.11):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.0, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=176.37, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=264.39, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.12, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.24, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=176.37, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=215.49, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.94, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=264.39, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='12', width=293.35):
            with Note(default_x=17.23, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.14, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=103.05, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.43, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=195.2, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.02, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=248.84, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=60.14, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=103.05, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=150.43, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.2, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=248.84, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=114.05, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=157.43, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=200.2, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
        with Measure(number='13', width=291.38):
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=101.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=153.97, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=195.76, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=254.99, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=25.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=112.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
            with Note(default_x=153.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=195.76, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=247.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=25.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=67.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.18, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=142.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=243.99, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
        with Measure(number='14', width=325.0):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=140.48, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=219.6, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=30.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=130.48, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=173.9, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=219.6, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.44, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=278.84, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=30.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='stop', number=2)
            with Note(default_x=74.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=102.64, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=130.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=186.04, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=278.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
        with Measure(number='15', width=282.57):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=55.2, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=89.63, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=166.06, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=89.63, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=111.16, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=132.68, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=169.06, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=246.54, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=63.2, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=132.68, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=169.06, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.49, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=225.01, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=246.54, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='16', width=232.24):
            with Note(default_x=12.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=109.63, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.02, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=113.63, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=198.02, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.41, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.02, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.63, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=146.25, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=198.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='17', width=222.4):
            with Note(default_x=15.8, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=49.97, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=49.97, default_y=-5.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=84.13, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=84.13, default_y=-10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=118.3, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=118.3, default_y=-10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=152.47, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=152.47, default_y=-15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=186.64, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=186.64, default_y=-20.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=49.97, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=84.13, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=118.3, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=152.47, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=186.64, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='18', width=242.73):
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=132.07, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=168.42, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=204.78, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=23.0, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=132.07, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=38.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.36, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=95.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=204.78, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
        with Measure(number='19', width=234.89):
            with Note(default_x=15.8, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.05, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=88.3, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=124.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=20.8, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=127.55, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.05, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=88.3, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=124.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.79, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=197.04, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='20', width=352.72):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=70.0, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=109.93, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=141.32, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=166.28, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=206.2, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=211.2, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=249.43, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.24, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=311.19, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=75.0, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=109.93, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=166.28, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.2, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='21', width=214.92):
            with Note(default_x=25.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=54.65, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=72.68, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.71, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.74, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=126.77, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=30.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.71, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=126.77, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=155.62, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=184.47, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='22', width=204.11):
            with Note(default_x=12.12, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.41, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=59.72, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.02, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=96.33, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.64, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=114.64, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.93, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=173.22, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=41.41, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=78.02, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='23', width=231.7):
            with Note(default_x=15.8, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.24, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=66.88, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.53, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.18, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=125.83, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=167.22, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=198.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.83, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=167.22, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=198.66, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=47.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.53, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.83, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.66, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='24', width=211.38):
            with Note(default_x=17.0, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.49, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=77.98, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.38, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=148.8, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.29, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=109.38, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=179.29, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='25', width=289.9):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=72.24, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=117.44, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=151.61, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=185.78, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=219.95, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=254.13, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=67.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=185.78, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=82.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=254.13, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='26', width=300.11):
            with Note(default_x=12.0, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=130.01, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=27.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=95.67, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=150.9, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=259.18, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=51.34, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=90.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.9, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=203.2, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.59, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=259.18, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='27', width=208.41):
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=46.81, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.81, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=108.82, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=139.83, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=175.8, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=108.82, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=139.83, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=175.8, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='28', width=241.53):
            with Note(default_x=17.23, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=133.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=96.25, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=133.06, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=168.68, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=204.31, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=55.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=91.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=138.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
        with Measure(number='29', width=174.88):
            with Note(default_x=17.0, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=43.05, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=69.09, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=95.14, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=121.19, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.24, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=95.14, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=121.19, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=147.24, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='30', width=273.19):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.0, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=129.86, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=165.3, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=134.86, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=165.3, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=200.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=236.16, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=94.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=129.86, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.3, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='31', width=249.83):
            with Note(default_x=12.0, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=49.8, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=87.59, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.39, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=163.19, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=186.81, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=210.43, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=125.39, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=163.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=210.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=332.74):
            with Note(default_x=30.13, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=126.04, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=183.01, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=228.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=257.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=285.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.06, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=97.55, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.04, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.52, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=188.01, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=32.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=183.01, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=285.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
        with Measure(number='33', width=359.07):
            with Note(default_x=37.0, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=75.16, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=135.73, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=182.41, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=211.59, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=240.76, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.94, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=299.11, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=328.29, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=23.87, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=182.41, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=240.76, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=299.11, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=23.87, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=75.16, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=106.56, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=135.73, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=182.41, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='34', width=322.95):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=55.2, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=77.29, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.38, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.47, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=143.56, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.65, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=187.74, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=209.83, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.92, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.01, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.1, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.19, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=99.38, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=143.56, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=187.74, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=231.92, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=276.1, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='35', width=191.22):
            with Note(default_x=15.8, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=44.77, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=73.74, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=102.71, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=102.71, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(2.0)
            with Note(default_x=44.77, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.74, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=131.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.65, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='36', width=196.64):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=42.1, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=72.09, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=105.09, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=105.09, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=42.1, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.09, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=135.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=165.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='37', width=245.84):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=53.31, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=90.82, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=138.33, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=206.73, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=90.82, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=140.19, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=206.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Forward():
                Duration(4.0)
            with Note(default_x=90.82, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.19, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=169.22, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=201.73, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
        with Measure(number='38', width=258.17):
            with Note(default_x=37.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=154.95, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=188.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=222.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=23.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=87.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=154.95, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=33.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=169.95, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=188.82, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=222.7, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='39', width=239.89):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=60.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=89.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=119.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=149.24, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=178.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=208.61, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=60.2, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=89.88, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=119.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=149.24, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=178.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=144.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='40', width=245.13):
            with Note(default_x=12.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.25, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=87.65, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=131.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=156.15, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=177.55, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.96, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.36, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=46.25, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=87.65, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.9, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=77.65, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=121.9, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Forward():
                Duration(2.0)
        with Measure(number='41', width=282.78):
            with Note(default_x=15.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.82, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.84, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.86, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.88, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.9, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.92, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.93, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.95, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.97, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.99, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.01, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=147.92, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
        with Measure(number='42', width=210.09):
            with Note(default_x=15.44, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=47.92, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=112.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=144.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=176.38, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='43', width=236.95):
            with Note(default_x=12.0, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Tie(type='stop')
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='stop')
                    Tied(type='start')
            with Note(default_x=123.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=160.9, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=198.12, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=49.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=86.45, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=123.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=160.9, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=198.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='44', width=260.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(149.18)
            with Note(default_x=59.0, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Note(default_x=158.83, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=192.11, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=225.39, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=158.83, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Tie(type='stop')
                Voice('2')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=230.39, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=92.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.55, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=158.83, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=192.11, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=225.39, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='45', width=225.45):
            with Note(default_x=17.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=124.58, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=124.58, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.67, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=190.76, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=50.09, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=83.18, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=114.58, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='46', width=204.8):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=109.6, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=114.6, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=47.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=78.2, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=109.6, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=140.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=172.0, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='47', width=256.48):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.07, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=88.34, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=125.11, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=164.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=195.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=218.61, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=88.34, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=125.11, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=98.34, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
            with Note(default_x=125.11, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=164.54, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=218.61, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='48', width=267.84):
            with Note(default_x=17.0, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=57.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=87.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=123.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.48, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=199.88, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('continue', number=1)
                with Notations():
                    with Ornaments():
                        TrillMark()
            with Note(default_x=243.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=47.43, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=118.28, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=199.88, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.43, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=87.86, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=133.28, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('down')
        with Measure(number='49', width=319.76):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(162.93)
            with Direction(placement='above'):
                with DirectionType():
                    Words('[fine]', default_y=28.2, relative_x=-10.5, relative_y=35.8)
            with Note(default_x=59.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=40.61)
            with Note(default_x=130.49, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=170.43, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=192.77, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.97, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.31, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.65, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.99, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=59.0, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Backup():
                Duration(12.0)
            with Note(default_x=69.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.75, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=130.49, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.43, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=227.97, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Direction(placement='above'):
                with DirectionType():
                    Words('Fine', default_y=17.85, relative_y=20.0)
                Sound(fine='yes')
        with Measure(number='50', width=288.86):
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.15, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=58.5, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.89, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.24, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.59, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.93, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.28, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=196.63, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.98, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.32, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.09, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.24, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=153.93, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=239.32, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='51', width=345.68):
            with Note(default_x=15.8, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.9, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.01, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.11, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=124.21, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=167.67, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=208.57, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.67, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.77, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.88, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.98, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note(default_x=119.21, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=154.54, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=230.67, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.01, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.21, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=179.54, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.67, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=289.88, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='52', width=260.53):
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=35.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.79, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.79, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=95.79, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.79, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.78, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=155.78, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.78, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.77, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.77, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.77, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=95.79, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=135.78, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=175.78, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=215.77, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='53', width=428.97):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(149.18)
            with Note(default_x=59.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=89.7, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.4, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.09, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.79, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.49, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=243.19, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=273.88, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.58, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.28, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=365.98, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=396.67, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=181.79, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=243.19, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=365.98, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='54', width=363.74):
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=45.15, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.51, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.86, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.06, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.41, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=197.76, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.12, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.47, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.83, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=315.18, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.06, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=197.76, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=256.47, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=315.18, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='55', width=422.12):
            with Note(default_x=29.26, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=116.96, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=150.69, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.41, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.14, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=251.87, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.6, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.33, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=353.06, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=386.79, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=39.26, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=83.23, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=150.69, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=218.14, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=285.6, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=353.06, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=29.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=29.26, default_y=-10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
        with Measure(number='56', width=370.96):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(149.18)
            with Note(default_x=59.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=98.51, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=147.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=207.79, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=270.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=319.97, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=98.51, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=123.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.9, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.79, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=239.19, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=270.58, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.97, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='57', width=291.51):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.86, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=104.48, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=148.1, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=191.73, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=244.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.04, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.86, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=82.67, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.48, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.29, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.1, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.92, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.73, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.94, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.75, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='58', width=342.49):
            with Note(default_x=21.03, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=52.43, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=76.24, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.63, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.83, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=166.64, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.04, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=221.85, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.65, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=269.46, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=293.27, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=317.08, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.03, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=76.24, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=142.83, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=198.04, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=293.27, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='59', width=209.87):
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=46.93, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=78.06, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=109.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=146.0, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=177.14, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(6.0)
                Tie(type='start')
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=109.2, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=146.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=177.14, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='60', width=417.62):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(149.18)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=98.39, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.59, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=160.94, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.34, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.69, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=275.21, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=302.57, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.92, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=361.32, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=388.67, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=71.04, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=133.59, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.34, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=247.86, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=302.57, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=361.32, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=71.04, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('down')
            with Note(default_x=247.86, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('down')
        with Measure(number='61', width=307.55):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=166.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=191.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.21, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.6, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.27, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=58.31, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.39, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=140.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=191.81, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=254.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note():
                Rest()
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note(default_x=140.46, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
        with Measure(number='62', width=227.0):
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.72, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=80.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=111.7, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=143.19, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=162.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=182.55, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=202.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=48.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=80.21, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=111.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.19, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=182.55, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='63', width=262.66):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=38.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=61.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.93, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.64, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=129.35, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=152.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=224.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=152.06, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=188.39, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=224.73, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=66.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=111.64, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=152.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=188.39, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=224.73, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='64', width=489.73):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(149.18)
            with Note(default_x=67.24, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=102.44, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=137.63, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.67, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=207.7, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.73, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                Rest()
                Duration(1.0)
                Voice('1')
                Type('16th')
            with Note(default_x=312.96, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=348.0, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=383.03, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=418.06, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=453.1, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=67.24, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=137.63, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=207.7, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=277.77, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=348.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=418.06, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=72.24, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=282.77, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=72.24, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('4')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('4')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('4')
                Type('eighth')
            with Note(default_x=282.77, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('4')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('4')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('4')
                Type('eighth')
        with Measure(number='65', width=396.34):
            with Note(default_x=17.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=73.07, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=128.91, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=184.75, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=219.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=254.84, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.74, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=359.84, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.07, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=128.91, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.75, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=254.84, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=324.94, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Note(default_x=189.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
        with Measure(number='66', width=328.77):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=112.6, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=160.28, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=207.96, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.76, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=267.56, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.37, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=64.91, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=112.6, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Tie(type='start')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=160.28, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Tie(type='stop')
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.96, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=267.56, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=64.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=112.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=155.28, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note(default_x=202.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('up')
        with Measure(number='67', width=332.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(149.18)
            with Note(default_x=55.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=195.02, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=217.49, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.96, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.43, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=307.37, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=239.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=284.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=65.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.67, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=105.14, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.61, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.08, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=172.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='68', width=322.06):
            with Note(default_x=20.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.39, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=74.78, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=98.17, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.56, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.95, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=180.14, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=203.53, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.92, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=250.3, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.69, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.08, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=20.0, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=74.78, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=121.56, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=180.14, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=226.92, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=273.69, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='69', width=282.21):
            with Note(default_x=15.8, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=37.77, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=59.74, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=81.7, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.67, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.64, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=147.61, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=169.58, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.54, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.51, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.48, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.45, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=191.54, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.48, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='70', width=278.41):
            with Note(default_x=12.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=33.97, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=55.94, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.9, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=99.87, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.84, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=143.81, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=165.78, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=187.74, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.71, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=231.68, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.65, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=55.94, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=99.87, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=143.81, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=187.74, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=231.68, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='71', width=459.14):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(149.18)
            with Note(default_x=59.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=92.21, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.42, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=158.64, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.85, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.06, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=258.27, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=291.48, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.7, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.91, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=391.12, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=424.33, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=125.42, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=191.85, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=258.27, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=324.7, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=391.12, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='72', width=382.04):
            with Note(default_x=12.0, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.7, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.41, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.11, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.81, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.52, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=196.22, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=226.93, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=257.63, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.33, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.04, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=349.74, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.41, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=134.81, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=196.22, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=257.63, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=319.04, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='73', width=373.65):
            with Note(default_x=12.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.0, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=72.01, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.01, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=132.02, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=162.02, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.02, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.03, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.03, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.03, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=312.04, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=342.04, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=72.01, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=132.02, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=192.02, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=252.03, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=312.04, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='74', width=406.09):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=55.2, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=83.85, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.5, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=141.15, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.8, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.45, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.1, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=255.75, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.15, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.54, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=347.19, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=375.84, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.5, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=169.8, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=227.1, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=287.15, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=347.19, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='75', width=417.04):
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=86.34, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=151.65, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=216.97, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=282.28, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=350.13, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=21.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.65, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=184.31, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=216.97, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.62, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.28, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=314.93, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.13, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=382.79, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='76', width=391.7):
            with Note(default_x=15.8, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=203.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=46.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.32, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=140.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.66, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=203.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=265.41, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.75, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.93, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='77', width=351.49):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=55.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=212.68, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.61, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=124.82, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=147.04, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.68, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.88, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.09, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=282.3, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.52, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.73, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='78', width=239.96):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=47.8, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=79.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=111.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=143.8, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.2, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=215.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=79.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=111.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=143.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=195.2, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=20.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
        with Measure(number='79', width=277.99):
            with Note(default_x=15.8, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=119.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=87.7, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=124.1, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=166.5, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=206.83, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=51.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=87.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=135.1, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=172.5, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=189.66, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.83, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=253.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='80', width=345.38):
            with Note(default_x=17.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.68, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=97.08, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=132.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=183.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=207.62, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.79, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.01, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=295.34, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.68, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=132.4, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=183.4, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=235.79, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=295.34, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=127.4, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.63, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=183.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=290.34, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=319.56, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='81', width=420.26):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=59.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=85.96, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.91, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.87, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=175.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=243.55, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=270.51, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.47, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=364.75, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.91, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=175.2, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=243.55, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=297.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=364.75, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=170.2, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=202.16, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=233.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=354.75, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=391.71, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='82', width=327.68):
            with Note(default_x=15.8, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=40.55, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.3, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.05, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.55, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=164.29, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=189.04, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=220.44, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.19, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.59, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=301.33, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=15.8, default_y=-40.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=164.29, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=164.29, default_y=-40.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
        with Measure(number='83', width=231.54):
            with Note(default_x=29.26, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=29.26, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=62.71, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=62.71, default_y=0.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=96.15, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=96.15, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=129.6, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=129.6, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=163.05, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=163.05, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=196.49, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=196.49, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=29.26, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
        with Measure(number='84', width=235.35):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=52.12, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=52.12, default_y=5.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=88.45, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=88.45, default_y=10.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=124.77, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=124.77, default_y=15.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=161.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=161.1, default_y=-10.0):
                Chord()
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=197.42, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=197.42, default_y=-5.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
        with Measure(number='85', width=421.93):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=108.7, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.76, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=201.89, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=264.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.41, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=326.47, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=357.87, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=389.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=295.41, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=357.87, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='86', width=394.38):
            with Note(default_x=26.03, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=55.05, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=90.24, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=119.26, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=148.27, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.29, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=247.7, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.73, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=334.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=363.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=26.03, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=90.24, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=148.27, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=218.69, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=334.75, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=21.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=208.69, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='87', width=398.53):
            with Note(default_x=22.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=53.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.04, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.29, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=244.85, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=275.27, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=305.68, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=336.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=366.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=144.87, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=213.46, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=336.1, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=203.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('natural')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='88', width=331.43):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=60.2, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=81.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=102.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=144.71, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.83, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=222.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=243.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.41, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=285.54, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.66, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=60.2, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=102.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=144.71, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=201.03, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=243.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=285.54, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
        with Measure(number='89', width=263.31):
            with Note(default_x=12.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.59, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=53.19, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.78, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.38, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=114.97, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.57, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=156.16, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.76, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=197.35, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=217.95, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.54, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=53.19, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=94.38, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=135.57, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=176.76, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=217.95, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='90', width=281.69):
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.88, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=57.95, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=79.03, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.1, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=121.18, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=142.26, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=163.33, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=193.7, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=214.77, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.85, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=256.93, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=57.95, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=100.1, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=142.26, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=193.7, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=235.85, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='91', width=338.41):
            with Note(default_x=15.8, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.28, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=70.67, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=94.15, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=125.55, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.03, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=184.22, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=207.7, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=242.9, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.37, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.85, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=313.33, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=70.67, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=125.55, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=184.22, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=242.9, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=289.85, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='92', width=379.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=59.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.53, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.07, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.6, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=165.13, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=191.67, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=218.2, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=244.73, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=271.27, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.33, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=350.87, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=112.07, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=165.13, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=218.2, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=271.27, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=324.33, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='93', width=251.74):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.05, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=94.87, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=133.69, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=172.51, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=211.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=56.05, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=133.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=172.51, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=211.33, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='94', width=251.53):
            with Note():
                with Rest():
                    DisplayStep('F')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=51.75, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=91.39, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=131.03, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=170.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=210.3, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=51.75, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=91.39, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=131.03, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.66, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=210.3, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=12.12, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('D')
                    DisplayOctave(2)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(1)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='95', width=332.56):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('eighth')
            with Note(default_x=58.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=85.4, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=112.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.94, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=165.71, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=192.48, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=219.25, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=246.02, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=277.42, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=304.19, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=219.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=277.42, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='96', width=408.78):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=71.04, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=98.74, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=126.45, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.15, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.85, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.56, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=245.95, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=268.66, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=296.36, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=324.07, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.77, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=379.47, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=71.04, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=126.45, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=181.85, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=240.95, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=351.77, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(4)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=240.95, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Stem('up')
        with Measure(number='97', width=414.08):
            with Note(default_x=22.23, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.85, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.46, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=109.08, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=139.69, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=170.31, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=215.93, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=254.12, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=279.73, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=310.35, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=340.96, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=381.86, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.69, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=201.82, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=352.83, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Forward():
                Duration(2.0)
            with Note(default_x=200.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('3')
                Type('quarter')
                Dot()
                Accidental('natural')
                Stem('up')
        with Measure(number='98', width=391.98):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=201.19, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=43.53, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=75.06, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=106.6, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.13, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=169.66, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=201.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=232.72, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=327.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=358.85, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='99', width=343.48):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(0.0)
                    SystemDistance(129.54)
            with Note(default_x=70.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=212.56, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(12.0)
            with Note(default_x=70.21, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=95.4, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=115.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=135.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.12, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=176.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=212.56, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=237.76, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=278.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=298.48, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=318.72, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='100', width=238.4):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=48.51, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=81.22, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=113.94, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=146.94, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=167.91, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=192.67, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.64, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=81.22, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=113.94, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=146.94, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.67, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(5)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
        with Measure(number='101', width=285.68):
            with Note(default_x=15.8, default_y=20.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
            with Note(default_x=138.63, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=92.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=138.63, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=194.22, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=239.95, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note():
                with Rest():
                    DisplayStep('B')
                    DisplayOctave(5)
                Duration(2.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=49.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=82.69, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=119.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=194.22, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=215.19, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=239.95, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.92, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='102', width=347.26):
            with Note(default_x=15.8, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=41.47, default_y=15.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=67.13, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=100.14, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=130.46, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=182.9, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=208.57, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=238.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=264.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=294.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=67.13, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=135.46, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=182.9, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=238.33, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=294.33, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=130.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=156.13, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=182.9, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=294.33, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=319.99, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='103', width=446.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(129.54)
            with Note(default_x=59.0, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=91.19, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=123.39, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=155.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=187.77, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=252.16, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=284.35, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=348.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=380.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=123.39, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=192.77, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=252.16, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=316.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=385.93, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=59.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=187.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=219.96, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=252.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('quarter')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=380.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=413.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='104', width=382.97):
            with Note(default_x=17.0, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Tie(type='stop')
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=47.27, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=77.54, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.81, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=138.08, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.35, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.62, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.89, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.16, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=289.43, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=320.83, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=351.1, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.0, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note():
                Rest()
                Duration(6.0)
                Voice('2')
                Type('quarter')
                Dot()
            with Backup():
                Duration(12.0)
            with Note(default_x=12.0, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('eighth')
                Stem('down')
            with Forward():
                Duration(10.0)
        with Measure(number='105', width=384.95):
            with Note(default_x=22.23, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(3.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=102.18, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=137.37, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.12, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=198.87, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=260.36, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=291.11, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=321.86, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=352.61, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=22.23, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=71.43, default_y=-70.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=137.37, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=198.87, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=260.36, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=321.86, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('A')
                    DisplayOctave(0)
                Duration(4.0)
                Voice('3')
                Type('quarter')
        with Measure(number='106', width=360.89):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(130.21)
            with Note(default_x=55.2, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=103.46, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=151.72, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=207.25, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=262.77, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=311.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=55.2, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.33, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.46, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.59, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=151.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=175.85, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=207.25, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.64, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.77, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.9, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=311.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=335.16, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='107', width=291.47):
            with Note(default_x=17.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=62.59, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=107.95, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=153.31, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=198.67, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=244.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.91, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.59, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=85.27, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=107.95, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=153.31, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.99, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.67, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=221.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=244.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=266.71, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='108', width=374.93):
            with Note(default_x=17.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=48.63, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=80.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=111.42, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=142.82, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=171.63, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=200.45, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=229.26, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=286.89, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=315.7, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=344.52, default_y=5.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(12.0)
            with Note(default_x=17.23, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=80.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=142.82, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=315.7, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(2.0)
                Voice('2')
                Type('eighth')
                Stem('down')
        with Measure(number='109', width=187.53):
            with Note(default_x=15.8, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=42.27, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=68.74, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Direction(placement='below'):
                with DirectionType():
                    Words('[dal segno]\n', default_y=-50.64, relative_x=13.66, relative_y=-18.74)
                    Words('al Fine')
            with Note(default_x=95.22, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=121.69, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=148.16, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(12.0)
            with Note(default_x=15.8, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('quarter')
            with Note():
                Rest()
                Duration(2.0)
                Voice('2')
                Type('eighth')
            with Direction(placement='above'):
                with DirectionType():
                    Words('D.S. al Fine', default_y=17.55, relative_y=20.0)
                Sound(dalsegno='segno')
            with Barline(location='right'):
                BarStyle('light-heavy')