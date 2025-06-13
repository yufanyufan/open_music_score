with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('BWV 997')
    with Identification():
        Creator('Johann Sebastian Bach', type='composer')
        Rights('by Mutopia 2013/02/17-52\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ')
        with Encoding():
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
        CreditWords('3. Sarabande', default_x=671.355, default_y=1771.1, justify='center', valign='top', font_family='Times New Roman', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('Johann Sebastian Bach (1685-1750)\n', default_x=1278.77, default_y=1711.2, justify='right', valign='bottom', font_family='Times New Roman', font_size='12')
        CreditWords('BWV 997')
    with Credit(page=1):
        CreditType('rights')
        CreditWords('by Mutopia 2013/02/17-52\nScritto con MuseScore, un software libero e gratuito: http://musescore.org/it ', default_x=671.355, default_y=127.877, justify='center', valign='bottom', font_size='8')
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
        with Measure(number='1', width=326.51):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    TopSystemDistance(212.79)
            with Attributes():
                Divisions(8.0)
                with Key():
                    Fifths(0)
                with Time():
                    Beats('3')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-41.0, default_y=41.07, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('45')
                Sound(tempo=45.0)
            with Note(default_x=81.26, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=124.88, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=149.65, default_y=20.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=174.41, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=212.04, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=249.66, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=287.29, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=81.26, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.41, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=249.66, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=76.26, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=76.26, default_y=-5.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=174.41, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=212.04, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=249.66, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=287.29, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='2', width=277.17):
            with Note(default_x=22.36, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=22.36, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.42, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=93.18, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=117.95, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=157.35, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=196.76, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=236.17, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.36, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=12.36, default_y=-20.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='3', width=311.02):
            with Note(default_x=17.0, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=41.92, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=66.83, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.75, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=128.14, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=176.75, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('backward hook', number=2)
            with Note(default_x=209.76, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=234.67, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=259.59, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=284.5, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.0, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=128.14, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=209.76, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=12.0, default_y=-20.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=123.14, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=123.14, default_y=-10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('3')
                Type('quarter')
        with Measure(number='4', width=300.13):
            with Note(default_x=15.8, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=39.36, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.92, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=86.48, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=110.04, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=133.6, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=157.16, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.72, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.28, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=227.84, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=251.4, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=274.97, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
        with Measure(number='5', width=354.76):
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
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=82.21, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('end', number=2)
            with Note(default_x=113.6, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='start')
            with Note(default_x=150.73, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('eighth')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(24.0)
            with Note(default_x=59.0, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=150.73, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=260.33, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=113.6, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('3')
                Type('eighth')
                Stem('down')
                with Notations():
                    Tied(type='start')
            with Note(default_x=145.73, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Tie(type='stop')
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=190.71, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Accidental('flat')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=213.92, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=237.12, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=260.33, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.54, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=306.74, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=329.95, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('3')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='6', width=305.67):
            with Note(default_x=15.8, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.2, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.68, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=101.07, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.55, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=146.03, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.51, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=190.99, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.47, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=235.95, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=258.43, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=280.91, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=123.55, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=213.47, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=369.22):
            with Note(default_x=15.8, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.14, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.54, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.73, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=135.07, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.08, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.42, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=225.81, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=252.15, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=283.55, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=309.89, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=341.28, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=135.07, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=252.15, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='8', width=185.18):
            with Note(default_x=17.23, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=17.23, default_y=-25.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=17.23, default_y=-15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=64.76, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=64.76, default_y=-20.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note():
                Rest()
                Duration(8.0)
                Voice('1')
                Type('quarter')
            with Backup():
                Duration(24.0)
            with Note(default_x=17.23, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=64.76, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=94.47, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=124.17, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=153.88, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='9', width=347.46):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=81.55, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=104.1, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=126.65, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=149.2, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=171.75, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=194.3, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=216.86, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=239.41, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=261.96, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=297.93, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=322.69, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=59.0, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=149.2, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=239.41, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
        with Measure(number='10', width=293.87):
            with Note(default_x=20.0, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=41.87, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.75, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=85.62, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=107.49, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=129.37, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=151.24, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=181.61, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=203.48, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=225.35, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.23, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=269.1, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=20.0, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=151.24, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=203.48, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=247.23, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='11', width=281.67):
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.37, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=63.82, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=85.27, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=106.73, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=128.18, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=149.63, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=171.09, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=192.54, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=213.99, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=235.45, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.9, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=106.73, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=192.54, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
        with Measure(number='12', width=291.84):
            with Note(default_x=21.03, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=42.5, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=63.96, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=95.36, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.82, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=138.29, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=159.75, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=181.21, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=202.68, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=224.14, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=245.61, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=267.07, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=21.03, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=159.75, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=202.68, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=245.61, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='13', width=344.91):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=55.2, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.21, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=103.22, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=127.23, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=151.24, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=175.24, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.25, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=223.26, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=247.27, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=271.28, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=295.29, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=319.3, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=55.2, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=199.25, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.27, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=295.29, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=301.71):
            with Note(default_x=12.0, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=36.01, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=60.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=84.03, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=108.04, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=132.04, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=156.05, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=180.06, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=204.07, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=228.08, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=252.09, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.1, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('G')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=156.05, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=204.07, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=252.09, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='15', width=313.9):
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=40.51, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=65.22, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=89.93, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=114.63, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=139.34, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=164.05, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=188.76, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=213.47, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=238.18, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=262.89, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=287.6, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=65.22, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=114.63, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=164.05, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=213.47, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=262.89, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='16', width=254.32):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=29.9)
            with Note(default_x=15.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.06, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=88.32, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=124.58, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=160.84, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=197.1, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='17', width=142.69):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Barline(location='left'):
                Ending(None, number='2', type='start', default_y=29.9)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=59.0, default_y=-40.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=59.0, default_y=-30.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=59.0, default_y=-15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                Ending(None, number='2', type='stop')
        with Measure(number='18', width=255.34):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=37.96, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=77.61, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.78, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=116.94, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=151.14, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=185.34, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=219.54, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=37.96, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=116.94, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=185.34, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=32.96, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=32.96, default_y=-15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=111.94, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=151.14, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=180.34, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=219.54, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='19', width=246.96):
            with Note(default_x=26.87, default_y=0.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Accidental('sharp')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=26.87, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(6.0)
                Voice('2')
                Type('eighth')
                Dot()
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=68.54, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=85.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('2')
                Type('32nd')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=102.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=138.49, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=174.12, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=209.74, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=16.87, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
            with Note(default_x=16.87, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('3')
                Type('half')
                Dot()
                Stem('down')
        with Measure(number='20', width=331.73):
            with Note(default_x=17.0, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('eighth')
                Dot()
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=60.08, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
                Beam('begin', number=3)
            with Note(default_x=84.84, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('32nd')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                Beam('end', number=3)
            with Note(default_x=109.61, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=136.63, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=168.02, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=195.04, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=222.06, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=249.08, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=276.09, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=303.11, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.0, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.61, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=222.06, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=12.0, default_y=-10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=109.61, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(1)
                Duration(4.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=276.09, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
        with Measure(number='21', width=238.11):
            with Note(default_x=17.0, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=42.2, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=62.87, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=83.54, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=104.21, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=170.36, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=170.36, default_y=15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=17.0, default_y=-65.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(12.0)
                Voice('2')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=137.28, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.36, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=203.43, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note(default_x=104.21, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('down')
            with Note():
                with Rest():
                    DisplayStep('C')
                    DisplayOctave(1)
                Duration(8.0)
                Voice('3')
                Type('quarter')
        with Measure(number='22', width=300.62):
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
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=59.0, default_y=15.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=99.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=99.0, default_y=10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=139.01, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=139.01, default_y=10.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=179.01, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=179.01, default_y=5.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=219.02, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=219.02, default_y=5.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Note(default_x=259.02, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=259.02, default_y=0.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(8.0)
                Voice('2')
                Type('quarter')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=259.02, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Backup():
                Duration(24.0)
            with Note():
                Rest()
                Duration(16.0)
                Voice('3')
                Type('half')
            with Note():
                Rest()
                Duration(4.0)
                Voice('3')
                Type('eighth')
            with Note():
                Rest()
                Duration(4.0)
                Voice('3')
                Type('eighth')
        with Measure(number='23', width=289.46):
            with Note(default_x=17.23, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=56.13, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=80.44, default_y=10.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=122.55, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=200.34, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=22.23, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=56.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=122.19, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=161.45, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=200.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=239.24, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=263.55, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('2')
                Type('16th')
                Stem('down')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=17.23, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=51.13, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=112.19, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(16.0)
                Voice('3')
                Type('half')
                Stem('down')
        with Measure(number='24', width=376.65):
            with Note(default_x=15.8, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.2, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=78.59, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=108.04, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=139.44, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=168.89, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=198.34, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=227.79, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=257.25, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=286.7, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=316.15, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=345.6, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=139.44, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note(default_x=257.25, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
        with Measure(number='25', width=248.1):
            with Note(default_x=15.8, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=92.34, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(16.0)
                Voice('1')
                Type('half')
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-75.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=54.25, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=92.7, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=131.15, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=169.6, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=208.05, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=20.8, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=20.8, default_y=-20.0):
                Chord()
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
            with Note(default_x=131.15, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=169.6, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=208.05, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('3')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='26', width=333.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=71.04, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=93.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=113.63, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=134.06, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=154.48, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=174.91, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=206.3, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=226.73, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=247.16, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=267.58, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=288.01, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=308.43, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=71.04, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=206.3, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=247.16, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=288.01, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=76.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note(default_x=76.04, default_y=-25.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('3')
                Type('quarter')
                Stem('up')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(5)
                Duration(8.0)
                Voice('3')
                Type('quarter')
            with Note():
                with Rest():
                    DisplayStep('E')
                    DisplayOctave(5)
                Duration(8.0)
                Voice('3')
                Type('quarter')
        with Measure(number='27', width=340.59):
            with Note(default_x=12.0, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=67.13, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=89.21, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=111.29, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.49, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=168.57, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=190.65, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=224.82, default_y=15.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=249.58, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=271.66, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=293.74, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=315.82, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=23.87, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=89.21, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=146.49, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Accidental('sharp')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=190.65, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=249.58, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=293.74, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='28', width=254.55):
            with Note(default_x=12.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=31.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=51.6, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.4, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=91.19, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=110.99, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=130.79, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=150.59, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=170.39, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=190.19, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=209.99, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=229.79, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=130.79, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=170.39, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=209.99, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='29', width=286.49):
            with Note(default_x=12.0, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=52.9, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.76, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=94.62, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.48, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=136.35, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=157.21, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=178.17, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=199.14, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=220.0, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=240.87, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=261.73, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Backup():
                Duration(24.0)
            with Note(default_x=23.87, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=73.76, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=115.48, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=157.21, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=199.14, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=240.87, default_y=-65.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='30', width=318.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(-0.0)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=59.0, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=79.36, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
                with Notations():
                    Slur(type='start', placement='above', number=1)
            with Note(default_x=99.73, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=120.09, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=140.45, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=160.82, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=181.18, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=212.58, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=232.94, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=253.31, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=273.67, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.03, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=59.0, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(8.0)
                Voice('2')
                Type('quarter')
                Stem('down')
            with Note():
                Rest()
                Duration(4.0)
                Voice('2')
                Type('eighth')
            with Note(default_x=181.18, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
            with Note(default_x=232.94, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=273.67, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='31', width=271.8):
            with Note(default_x=12.0, default_y=-35.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=32.36, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=52.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=73.09, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=93.45, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=134.18, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=154.55, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=174.91, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=206.31, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=226.67, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=247.03, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=12.0, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=52.73, default_y=-40.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=93.45, default_y=-45.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=134.18, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=174.91, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=226.67, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='32', width=319.7):
            with Note(default_x=15.8, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=47.2, default_y=5.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=69.59, default_y=10.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=91.99, default_y=0.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=123.39, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=145.79, default_y=-5.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=177.18, default_y=-30.0, dynamics=100.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=199.58, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=227.75, default_y=-10.0, dynamics=100.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
            with Note(default_x=250.14, default_y=-15.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=272.54, default_y=-20.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('continue', number=2)
            with Note(default_x=294.94, default_y=-25.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=69.59, default_y=-55.0, dynamics=100.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=123.39, default_y=-50.0, dynamics=100.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=177.18, default_y=-70.0, dynamics=100.0):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=227.75, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=272.54, default_y=-75.0, dynamics=100.0):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='33', width=215.36):
            with Barline(location='left'):
                Ending(None, number='1', type='start', default_y=29.9)
            with Note(default_x=15.44, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-30.0):
                Chord()
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.44, default_y=-15.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Backup():
                Duration(24.0)
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=45.57, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=75.33, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=105.1, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=134.87, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=164.64, default_y=-60.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('2')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='1', type='stop')
                Repeat(direction='backward')
        with Measure(number='34', width=89.17):
            with Barline(location='left'):
                Ending(None, number='3', type='start', default_y=29.9)
            with Note(default_x=15.8, default_y=-60.0, dynamics=100.0):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-50.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-40.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Note(default_x=15.8, default_y=-25.0, dynamics=100.0):
                Chord()
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(24.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Ending(None, number='3', type='stop')