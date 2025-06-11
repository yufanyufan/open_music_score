with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Leck mich im Arsch')
    with Identification():
        Creator('W. A. Mozart', type='composer')
        with Encoding():
            Software('MuseScore 3.6.2')
            EncodingDate('2025-01-13')
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
            PageHeight(1898.53)
            PageWidth(1343.09)
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
        CreditWords('Leck mich im Arsch', default_x=671.547, default_y=1834.59, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('subtitle')
        CreditWords('KV 231 (382c)', default_x=671.547, default_y=1770.65, justify='center', valign='top', font_size='14')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('W. A. Mozart', default_x=1279.15, default_y=1691.47, justify='right', valign='bottom', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('I')
            PartAbbreviation('I')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('II')
            PartAbbreviation('II')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('III')
            PartAbbreviation('III')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('IV')
            PartAbbreviation('IV')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P5'):
            PartName('V')
            PartAbbreviation('V')
            with ScoreInstrument(id='P5-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P5-I1', port=1)
            with MidiInstrument(id='P5-I1'):
                MidiChannel(5)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P6'):
            PartName('VI')
            PartAbbreviation('VI')
            with ScoreInstrument(id='P6-I1'):
                InstrumentName('Stemmer')
            MidiDevice(None, id='P6-I1', port=1)
            with MidiInstrument(id='P6-I1'):
                MidiChannel(6)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='1', width=175.49):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(24.08)
                        RightMargin(0.0)
                    TopSystemDistance(213.12)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-40.63, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('140')
                Sound(tempo=140.0)
            with Note(default_x=109.51, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='2', width=83.27):
            with Note(default_x=17.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='3', width=67.54):
            with Note(default_x=20.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='4', width=92.2):
            with Note(default_x=21.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='5', width=130.03):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=54.23, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='6', width=86.7):
            with Note(default_x=12.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=48.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='7', width=123.78):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=53.19, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='8', width=99.69):
            with Note(default_x=12.36, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.0, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='9', width=117.04):
            with Note(default_x=23.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=69.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='10', width=97.64):
            with Note(default_x=14.71, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=55.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='11', width=117.76):
            with Note(default_x=14.26, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=65.03, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-40.0, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(24.08)
                        RightMargin(0.0)
                    SystemDistance(86.63)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=139.18, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=178.97, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='13', width=219.3):
            with Note(default_x=30.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=80.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=126.23, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=171.96, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='14', width=189.79):
            with Note(default_x=15.8, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=58.9, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=101.99, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=145.09, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='15', width=212.7):
            with Note(default_x=23.01, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=70.03, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=117.05, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=164.08, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='16', width=349.99):
            with Note(default_x=16.92, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=84.58, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=128.99, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=171.28, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=221.54, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=263.82, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=306.1, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(24.08)
                        RightMargin(-0.0)
                    SystemDistance(99.51)
            with Note(default_x=87.21, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=116.93, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=146.29, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-47.24, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='18', width=322.04):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=71.35, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=111.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=160.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=210.91, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=247.42, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=283.93, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='19', width=120.59):
            with Note(default_x=12.0, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=41.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=71.08, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-47.24, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='20', width=189.14):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=49.25, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=5.34, default_y=-47.24, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=71.94, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=94.64, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=117.33, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=140.03, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-47.24, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='21', width=363.56):
            with Note(default_x=31.13, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=100.78, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=144.31, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=187.84, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=231.37, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=274.9, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=318.43, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(24.08)
                        RightMargin(0.0)
                    SystemDistance(102.22)
            with Note(default_x=87.21, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=172.28, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='23', width=476.23):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=110.14, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=170.89, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=231.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=292.38, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=353.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=413.88, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='24', width=319.85):
            with Note(default_x=12.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=97.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.78, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(39.42)
                        RightMargin(0.0)
                    SystemDistance(91.1)
            with Note(default_x=87.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='26', width=76.28):
            with Note(default_x=17.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='27', width=63.66):
            with Note(default_x=20.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='28', width=84.4):
            with Note(default_x=21.62, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='29', width=122.88):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=47.08, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='30', width=85.94):
            with Note(default_x=20.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=52.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='31', width=120.35):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=49.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='32', width=100.83):
            with Note(default_x=24.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=53.14, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='33', width=147.21):
            with Note(default_x=23.28, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=71.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='34', width=93.1):
            with Note(default_x=20.52, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=55.83, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='35', width=134.99):
            with Note(default_x=23.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=64.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-40.0, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    SystemDistance(86.63)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=113.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=152.95, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='37', width=180.3):
            with Note(default_x=30.23, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=80.49, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=112.31, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=143.53, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='38', width=155.97):
            with Note(default_x=20.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=53.81, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=94.84, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=124.02, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='39', width=171.95):
            with Note(default_x=23.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=56.68, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=94.36, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=137.47, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='40', width=292.59):
            with Note(default_x=24.94, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=62.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=106.41, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=147.48, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=197.74, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=229.57, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=256.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='41', width=180.3):
            with Note(default_x=30.23, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-55.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=80.49, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=111.95, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-55.49, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=135.48, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=175.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-42.82, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=224.78, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=275.04, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=306.87, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=334.67, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='43', width=181.9):
            with Note(default_x=23.79, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=61.59, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=99.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-42.82, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='44', width=300.93):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=70.39, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-42.82, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=114.81, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=155.88, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=206.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=237.96, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-42.82, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.98, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=91.66, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=128.33, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=165.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=202.47, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=239.93, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=278.1, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-42.82, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=91.01, default_y=5.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=162.9, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='47', width=356.32):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.46, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=137.0, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=180.55, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=224.09, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=267.63, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=311.18, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='48', width=374.12):
            with Note(default_x=24.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=97.02, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=186.76, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=87.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='50', width=376.35):
            with Note(default_x=17.56, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='51', width=358.8):
            with Note(default_x=20.47, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=87.69, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='53', width=371.74):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=191.36, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='54', width=368.19):
            with Note(default_x=20.52, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=184.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=246.9, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='56', width=374.07):
            with Note(default_x=24.58, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.73, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='57', width=377.37):
            with Note(default_x=30.77, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=194.02, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(-0.0)
                    SystemDistance(150.0)
            with Note(default_x=90.65, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=256.98, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='59', width=356.32):
            with Note(default_x=23.43, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=180.18, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='60', width=374.12):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=187.12, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=282.42, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=90.53, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=163.61, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=254.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=346.34, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='62', width=376.35):
            with Note(default_x=20.88, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.48, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=188.37, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=284.0, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='63', width=358.8):
            with Note(default_x=23.79, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=93.98, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=181.72, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=269.46, default_y=-50.0):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=91.01, default_y=-55.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=162.12, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=206.56, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=251.01, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=301.27, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=345.71, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=390.15, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='65', width=373.44):
            with Note(default_x=31.13, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-55.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=102.86, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=192.16, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-55.49, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='66', width=364.81):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=86.55, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=130.77, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=180.28, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=230.54, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=274.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=318.98, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(40.77)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=88.14, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-43.01, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=196.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=332.55, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-43.01, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='68', width=567.96):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=129.21, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-43.01, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=199.39, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=269.58, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-43.01, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=339.76, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=409.94, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-43.01, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P2'):
        with Measure(number='1', width=175.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=67.54):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=92.2):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=130.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=86.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=123.78):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=99.69):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=117.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=97.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=117.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=219.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=189.79):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=212.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=349.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=322.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=120.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=189.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=363.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-40.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=476.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=319.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.01)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=76.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=63.66):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=84.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=122.88):
            with Note(default_x=17.79, default_y=-141.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='30', width=85.94):
            with Note(default_x=17.56, default_y=-136.01):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='31', width=120.35):
            with Note(default_x=20.47, default_y=-146.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='32', width=100.83):
            with Note(default_x=21.62, default_y=-141.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='33', width=147.21):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=71.41, default_y=-141.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='34', width=93.1):
            with Note(default_x=20.52, default_y=-141.01):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=55.83, default_y=-146.01):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='35', width=134.99):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=64.4, default_y=-126.01):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.85)
            with Note(default_x=90.17, default_y=-139.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=112.8, default_y=-144.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-46.79, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='37', width=180.3):
            with Note(default_x=29.87, default_y=-144.85):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=111.95, default_y=-134.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='38', width=155.97):
            with Note(default_x=20.52, default_y=-139.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=94.48, default_y=-149.85):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='39', width=171.95):
            with Note(default_x=23.43, default_y=-134.85):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=94.0, default_y=-169.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='40', width=292.59):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=147.48, default_y=-154.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=229.57, default_y=-159.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='41', width=180.3):
            with Note(default_x=30.23, default_y=-164.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=80.49, default_y=-169.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=112.31, default_y=-174.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=143.53, default_y=-179.85):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.81)
            with Note(default_x=91.01, default_y=-176.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=135.48, default_y=-176.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=224.78, default_y=-161.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=306.87, default_y=-156.81):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='43', width=181.9):
            with Note(default_x=23.79, default_y=-161.81):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=61.59, default_y=-166.81):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=99.39, default_y=-171.81):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=142.49, default_y=-176.81):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='44', width=300.93):
            with Note(default_x=24.94, default_y=-181.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=70.39, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=114.81, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=155.88, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=206.14, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=237.96, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=266.37, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.98, default_y=-126.81):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-55.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=91.66, default_y=-146.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=164.65, default_y=-146.81):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-55.49, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.32)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=162.9, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=207.83, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-42.82, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=257.34, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=307.6, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=352.53, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=397.47, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='47', width=356.32):
            with Note(default_x=23.79, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.46, default_y=-155.32):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.18, default_y=-155.32):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-42.82, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='48', width=374.12):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.02, default_y=-150.32):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-42.82, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=142.07, default_y=-145.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=187.12, default_y=-140.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=237.38, default_y=-135.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=282.42, default_y=-130.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-42.82, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.1)
            with Note(default_x=90.53, default_y=-160.1):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=163.61, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=209.29, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=254.98, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=300.66, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=346.34, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=392.02, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='50', width=376.35):
            with Note(default_x=20.88, default_y=-125.1):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-43.49, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=93.48, default_y=-145.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.0, default_y=-145.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-43.49, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='51', width=358.8):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.98, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=137.85, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=181.72, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=225.59, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=269.46, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=313.33, default_y=-130.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.96)
            with Note(default_x=91.01, default_y=-124.96):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=161.64, default_y=-144.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=249.84, default_y=-144.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='53', width=371.74):
            with Note(default_x=27.81, default_y=-144.96):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-47.24, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='54', width=368.19):
            with Note(default_x=17.56, default_y=-139.96):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-47.24, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=87.21, default_y=-135.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='56', width=374.07):
            with Note(default_x=21.62, default_y=-130.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='57', width=377.37):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=194.02, default_y=-130.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.31)
            with Note(default_x=90.65, default_y=-146.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=256.98, default_y=-151.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='59', width=356.32):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=180.18, default_y=-131.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='60', width=374.12):
            with Note(default_x=24.58, default_y=-131.31):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.76, default_y=-136.31):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.84)
            with Note(default_x=90.17, default_y=-136.84):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=254.61, default_y=-126.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='62', width=376.35):
            with Note(default_x=20.52, default_y=-131.84):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=188.0, default_y=-141.84):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='63', width=358.8):
            with Note(default_x=23.43, default_y=-126.84):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=181.36, default_y=-161.84):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-40.0, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.85)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=251.01, default_y=-154.85):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=345.71, default_y=-159.85):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='65', width=373.44):
            with Note(default_x=31.13, default_y=-164.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=102.86, default_y=-169.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=192.52, default_y=-174.85):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=282.18, default_y=-179.85):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='66', width=364.81):
            with Note(default_x=15.8, default_y=-184.85):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=86.55, default_y=-184.85):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=180.28, default_y=-169.85):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=274.76, default_y=-164.85):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.39)
            with Note(default_x=88.14, default_y=-158.39):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=196.93, default_y=-163.39):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=332.91, default_y=-168.39):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=468.9, default_y=-173.39):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='68', width=567.96):
            with Note(default_x=16.92, default_y=-178.39):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=129.21, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=199.39, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=269.58, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=339.76, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=409.94, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=480.12, default_y=-123.39):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P3'):
        with Measure(number='1', width=175.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=67.54):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=92.2):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=130.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=86.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=123.78):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=99.69):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=117.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=97.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=117.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=219.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=189.79):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=212.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=349.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=322.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=120.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=189.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=363.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=476.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=319.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=76.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=63.66):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=84.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=122.88):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=85.94):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=120.35):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=100.83):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=147.21):
            with Note(default_x=20.32, default_y=-251.86):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='34', width=93.1):
            with Note(default_x=17.56, default_y=-246.86):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='35', width=134.99):
            with Note(default_x=20.47, default_y=-256.86):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.08)
            with Note(default_x=87.21, default_y=-283.93):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='37', width=180.3):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=111.95, default_y=-283.93):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='38', width=155.97):
            with Note(default_x=20.52, default_y=-283.93):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=94.48, default_y=-288.93):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='39', width=171.95):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=94.0, default_y=-268.93):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='40', width=292.59):
            with Note(default_x=24.58, default_y=-268.93):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=147.12, default_y=-273.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='41', width=180.3):
            with Note(default_x=29.87, default_y=-273.93):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=111.95, default_y=-263.93):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.85)
            with Note(default_x=90.65, default_y=-266.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=224.42, default_y=-276.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='43', width=181.9):
            with Note(default_x=23.43, default_y=-261.66):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=99.03, default_y=-296.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='44', width=300.93):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=155.88, default_y=-281.66):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=237.96, default_y=-286.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.98, default_y=-291.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=91.66, default_y=-296.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=165.01, default_y=-301.66):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=239.93, default_y=-306.66):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.2)
            with Note(default_x=91.01, default_y=-303.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=162.9, default_y=-303.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=257.34, default_y=-288.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=352.53, default_y=-283.51):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='47', width=356.32):
            with Note(default_x=23.79, default_y=-288.51):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=93.46, default_y=-293.51):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=180.55, default_y=-298.51):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=267.63, default_y=-303.51):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='48', width=374.12):
            with Note(default_x=24.94, default_y=-308.51):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=97.02, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=142.07, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=187.12, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=237.38, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=282.42, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=327.47, default_y=-253.51):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.62)
            with Note(default_x=90.53, default_y=-258.72):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=163.61, default_y=-278.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.61, default_y=-278.72):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-47.24, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='50', width=376.35):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.48, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=138.86, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=188.37, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=238.62, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=284.0, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=329.37, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='51', width=358.8):
            with Note(default_x=23.79, default_y=-263.72):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.98, default_y=-283.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.36, default_y=-283.72):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-47.24, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(97.17)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=161.64, default_y=-282.13):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-43.49, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=206.06, default_y=-277.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=250.2, default_y=-272.13):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-43.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=300.46, default_y=-267.13):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=344.61, default_y=-262.13):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-43.49, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='53', width=371.74):
            with Note(default_x=31.13, default_y=-292.13):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=102.5, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=147.11, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=191.72, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=236.32, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=280.93, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=325.54, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='54', width=368.19):
            with Note(default_x=20.88, default_y=-257.13):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-43.49, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=91.15, default_y=-277.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=184.22, default_y=-277.13):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-43.49, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(85.06)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=160.19, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=203.72, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=247.26, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=290.8, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=334.33, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=377.87, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='56', width=374.07):
            with Note(default_x=24.94, default_y=-235.91):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=97.01, default_y=-255.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=186.73, default_y=-255.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='57', width=377.37):
            with Note(default_x=27.81, default_y=-255.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-47.24, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=87.69, default_y=-252.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='59', width=356.32):
            with Note(default_x=20.47, default_y=-262.16):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='60', width=374.12):
            with Note(default_x=21.62, default_y=-257.16):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.08)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=254.61, default_y=-267.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='62', width=376.35):
            with Note(default_x=20.52, default_y=-267.92):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=188.0, default_y=-272.92):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='63', width=358.8):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=181.36, default_y=-252.92):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.84)
            with Note(default_x=90.65, default_y=-266.69):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=250.65, default_y=-271.69):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='65', width=373.44):
            with Note(default_x=30.77, default_y=-271.69):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=192.16, default_y=-261.69):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='66', width=364.81):
            with Note(default_x=15.44, default_y=-266.69):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=179.92, default_y=-276.69):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.09)
            with Note(default_x=87.78, default_y=-257.48):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=332.55, default_y=-292.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='68', width=567.96):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=269.58, default_y=-277.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=409.94, default_y=-282.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P4'):
        with Measure(number='1', width=175.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=67.54):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=92.2):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=130.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=86.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=123.78):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=99.69):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=117.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=97.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=117.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=219.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=189.79):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=212.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=349.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=322.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=120.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=189.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=363.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=476.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=319.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-271.86)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=76.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=63.66):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=84.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=122.88):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=85.94):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=120.35):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=100.83):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=147.21):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=93.1):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=134.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=180.3):
            with Note(default_x=26.91, default_y=-394.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='38', width=155.97):
            with Note(default_x=17.56, default_y=-389.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='39', width=171.95):
            with Note(default_x=20.47, default_y=-399.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='40', width=292.59):
            with Note(default_x=21.62, default_y=-394.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='41', width=180.3):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=111.95, default_y=-394.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(89.08)
            with Note(default_x=90.65, default_y=-410.75):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=224.42, default_y=-415.75):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='43', width=181.9):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=99.03, default_y=-395.75):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='44', width=300.93):
            with Note(default_x=24.58, default_y=-395.75):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=155.52, default_y=-400.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=32.61, default_y=-400.75):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=164.65, default_y=-390.75):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.09)
            with Note(default_x=90.65, default_y=-392.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=256.98, default_y=-402.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='47', width=356.32):
            with Note(default_x=23.43, default_y=-387.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=180.18, default_y=-422.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='48', width=374.12):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=187.12, default_y=-407.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=282.42, default_y=-412.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.6)
            with Note(default_x=90.53, default_y=-415.32):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=163.61, default_y=-420.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=254.98, default_y=-425.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=346.34, default_y=-430.32):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='50', width=376.35):
            with Note(default_x=20.88, default_y=-435.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.48, default_y=-435.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=188.37, default_y=-420.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=284.0, default_y=-415.32):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='51', width=358.8):
            with Note(default_x=23.79, default_y=-420.32):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=93.98, default_y=-425.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=181.72, default_y=-430.32):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=269.46, default_y=-435.32):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.5)
            with Note(default_x=91.01, default_y=-445.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=161.64, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=206.06, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=250.2, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=300.46, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=344.61, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=388.76, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='53', width=371.74):
            with Note(default_x=31.13, default_y=-390.63):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-55.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=102.5, default_y=-410.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=191.36, default_y=-410.63):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-55.49, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='54', width=368.19):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=91.15, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=135.07, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=184.58, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=234.84, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=278.76, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=322.67, default_y=-395.63):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.32)
            with Note(default_x=90.53, default_y=-371.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=160.19, default_y=-391.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=246.9, default_y=-391.23):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-42.82, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='56', width=374.07):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.01, default_y=-386.23):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-42.82, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=142.05, default_y=-381.23):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=187.09, default_y=-376.23):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=237.35, default_y=-371.23):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=282.39, default_y=-366.23):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-42.82, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='57', width=377.37):
            with Note(default_x=31.13, default_y=-396.23):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=103.69, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=149.03, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=194.38, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=239.73, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=285.08, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=330.42, default_y=-361.23):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-42.82, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.05)
            with Note(default_x=91.01, default_y=-362.21):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=162.9, default_y=-382.21):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=256.98, default_y=-382.21):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='59', width=356.32):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.46, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=137.0, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=180.55, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=224.09, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=267.63, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=311.18, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='60', width=374.12):
            with Note(default_x=24.94, default_y=-367.21):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=97.02, default_y=-387.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=186.76, default_y=-387.21):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=87.21, default_y=-378.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='62', width=376.35):
            with Note(default_x=17.56, default_y=-373.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='63', width=358.8):
            with Note(default_x=20.47, default_y=-383.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(78.6)
            with Note(default_x=87.69, default_y=-400.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='65', width=373.44):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=192.16, default_y=-400.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='66', width=364.81):
            with Note(default_x=15.44, default_y=-400.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=179.92, default_y=-405.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.4)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=332.55, default_y=-386.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='68', width=567.96):
            with Note(default_x=16.56, default_y=-386.88):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=269.22, default_y=-391.88):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P5'):
        with Measure(number='1', width=175.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=67.54):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=92.2):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=130.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=86.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=123.78):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=99.69):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=117.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=97.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=117.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=219.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=189.79):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=212.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=349.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=322.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=120.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=189.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=363.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=476.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=319.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=76.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=63.66):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=84.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=122.88):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=85.94):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=120.35):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=100.83):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=147.21):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=93.1):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=134.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=180.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=155.97):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='39', width=171.95):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='40', width=292.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=180.3):
            with Note(default_x=26.91, default_y=-505.64):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=87.69, default_y=-516.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='43', width=181.9):
            with Note(default_x=20.47, default_y=-526.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='44', width=300.93):
            with Note(default_x=21.62, default_y=-521.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=164.65, default_y=-521.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.31)
            with Note(default_x=90.65, default_y=-533.91):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=256.98, default_y=-538.91):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='47', width=356.32):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=180.18, default_y=-518.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='48', width=374.12):
            with Note(default_x=24.58, default_y=-518.91):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=186.76, default_y=-523.91):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.84)
            with Note(default_x=90.17, default_y=-522.16):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=254.61, default_y=-512.16):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='50', width=376.35):
            with Note(default_x=20.52, default_y=-517.16):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=188.0, default_y=-527.16):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='51', width=358.8):
            with Note(default_x=23.43, default_y=-512.16):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=181.36, default_y=-547.16):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-40.0, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.85)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=250.2, default_y=-545.48):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=344.61, default_y=-550.48):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='53', width=371.74):
            with Note(default_x=31.13, default_y=-555.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=102.5, default_y=-560.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=191.72, default_y=-565.48):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=280.93, default_y=-570.48):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='54', width=368.19):
            with Note(default_x=20.88, default_y=-575.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=91.15, default_y=-575.48):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-50.94, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=184.58, default_y=-560.48):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=278.76, default_y=-555.48):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.94, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.91)
            with Note(default_x=90.53, default_y=-529.14):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=160.19, default_y=-534.14):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=247.26, default_y=-539.14):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=334.33, default_y=-544.14):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='56', width=374.07):
            with Note(default_x=24.94, default_y=-549.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=97.01, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=142.05, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=187.09, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=237.35, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=282.39, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=327.43, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='57', width=377.37):
            with Note(default_x=31.13, default_y=-494.14):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-55.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=103.69, default_y=-514.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=194.02, default_y=-514.14):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-55.49, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.32)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=162.9, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=207.83, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-42.82, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=257.34, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=307.6, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=352.53, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=397.47, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-42.82, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='59', width=356.32):
            with Note(default_x=23.79, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.46, default_y=-522.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=180.18, default_y=-522.53):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-42.82, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='60', width=374.12):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=97.02, default_y=-517.53):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-42.82, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=142.07, default_y=-512.53):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=187.12, default_y=-507.53):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-42.82, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=237.38, default_y=-502.53):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=282.42, default_y=-497.53):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-42.82, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.1)
            with Note(default_x=90.53, default_y=-518.88):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=163.61, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=209.29, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=254.98, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=300.66, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=346.34, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=392.02, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='62', width=376.35):
            with Note(default_x=20.88, default_y=-483.88):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-43.49, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=93.48, default_y=-503.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=188.0, default_y=-503.88):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-43.49, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='63', width=358.8):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.98, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=137.85, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=181.72, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=225.59, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=269.46, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=313.33, default_y=-488.88):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(84.99)
            with Note(default_x=91.01, default_y=-505.28):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=162.12, default_y=-525.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=250.65, default_y=-525.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='65', width=373.44):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='66', width=364.81):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-421.88)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='68', width=567.96):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
    with Part(id='P6'):
        with Measure(number='1', width=175.49):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Attributes():
                Divisions(2.0)
                with Key():
                    Fifths(-2)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='2', width=83.27):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='3', width=67.54):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='4', width=92.2):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='5', width=130.03):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='6', width=86.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='7', width=123.78):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='8', width=99.69):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='9', width=117.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='10', width=97.64):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='11', width=117.76):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='12', width=219.35):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='13', width=219.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='14', width=189.79):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='15', width=212.7):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='16', width=349.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='17', width=195.8):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='18', width=322.04):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='19', width=120.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='20', width=189.14):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='21', width=363.56):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='22', width=395.05):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='23', width=476.23):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='24', width=319.85):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='25', width=146.15):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(0.0)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='26', width=76.28):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='27', width=63.66):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='28', width=84.4):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='29', width=122.88):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='30', width=85.94):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='31', width=120.35):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='32', width=100.83):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='33', width=147.21):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='34', width=93.1):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='35', width=134.99):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='36', width=193.33):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(-525.64)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='37', width=180.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='38', width=155.97):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='39', width=171.95):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='40', width=292.59):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='41', width=180.3):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='42', width=370.83):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='43', width=181.9):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='44', width=300.93):
            with Note():
                Rest(measure='yes')
                Duration(8.0)
                Voice('1')
        with Measure(number='45', width=320.78):
            with Barline(location='left'):
                BarStyle('heavy-light')
                Repeat(direction='forward')
            with Note(default_x=29.66, default_y=-632.45):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Leck')
        with Measure(number='46', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.85)
            with Note(default_x=87.69, default_y=-639.77):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('mich')
        with Measure(number='47', width=356.32):
            with Note(default_x=20.47, default_y=-649.77):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_y=-40.0, relative_x=-3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('im')
        with Measure(number='48', width=374.12):
            with Note(default_x=21.62, default_y=-644.77):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('whole')
                with Lyric(number='1', default_x=13.22, default_y=-40.0, relative_x=3.32, relative_y=-45.0):
                    Syllabic('single')
                    Text('Arsch')
        with Measure(number='49', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(81.08)
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=254.61, default_y=-653.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=12.03, default_y=-40.0, relative_x=12.03, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
                    Extend()
        with Measure(number='50', width=376.35):
            with Note(default_x=20.52, default_y=-653.25):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=188.0, default_y=-658.25):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=5.86, default_y=-40.0, relative_x=-0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
        with Measure(number='51', width=358.8):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=181.36, default_y=-638.25):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_x=10.77, default_y=-40.0, relative_x=10.77, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
        with Measure(number='52', width=434.5):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.84)
            with Note(default_x=90.65, default_y=-657.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('half')
                Stem('down')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=249.84, default_y=-662.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-40.0, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='53', width=371.74):
            with Note(default_x=30.77, default_y=-662.32):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Mur')
            with Note(default_x=191.36, default_y=-652.32):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren')
        with Measure(number='54', width=368.19):
            with Note(default_x=20.52, default_y=-657.32):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=184.22, default_y=-667.32):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-40.0, relative_x=0.36, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='55', width=423.01):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.85)
            with Note(default_x=90.17, default_y=-628.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=7.3, default_y=-46.79, relative_x=0.36, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=246.9, default_y=-663.99):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=11.38, default_y=-46.79, relative_x=2.27, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='56', width=374.07):
            with Note():
                Rest()
                Duration(4.0)
                Voice('1')
                Type('half')
            with Note(default_x=187.09, default_y=-648.99):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=282.39, default_y=-653.99):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.62, default_y=-46.79, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
        with Measure(number='57', width=377.37):
            with Note(default_x=31.13, default_y=-658.99):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=103.69, default_y=-663.99):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=194.38, default_y=-668.99):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=285.08, default_y=-673.99):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-46.79, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='58', width=444.0):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.2)
            with Note(default_x=91.01, default_y=-670.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=162.9, default_y=-670.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=257.34, default_y=-655.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=352.53, default_y=-650.73):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='59', width=356.32):
            with Note(default_x=23.79, default_y=-655.73):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('wah')
            with Note(default_x=93.46, default_y=-660.73):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('re')
            with Note(default_x=180.55, default_y=-665.73):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Kreuz')
            with Note(default_x=267.63, default_y=-670.73):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('des')
        with Measure(number='60', width=374.12):
            with Note(default_x=24.94, default_y=-675.73):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Le')
            with Note(default_x=97.02, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.72, default_y=-55.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
            with Note(default_x=142.07, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('das')
            with Note(default_x=187.12, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=237.38, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=282.42, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=327.47, default_y=-620.73):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-55.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='61', width=439.3):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.62)
            with Note(default_x=90.53, default_y=-617.5):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=163.61, default_y=-637.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=254.61, default_y=-637.5):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=11.44, default_y=-47.24, relative_x=2.05, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='62', width=376.35):
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=93.48, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Knur')
            with Note(default_x=138.86, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.62, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('ren,')
            with Note(default_x=188.37, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('Brum')
            with Note(default_x=238.62, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=284.0, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('ist')
            with Note(default_x=329.37, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
        with Measure(number='63', width=358.8):
            with Note(default_x=23.79, default_y=-622.5):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=1.44, default_y=-47.24, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=93.98, default_y=-642.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=181.36, default_y=-642.5):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=10.0, default_y=-47.24, relative_x=1.33, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens,')
        with Measure(number='64', width=436.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.32)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=162.12, default_y=-655.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=5.34, default_y=-43.49, relative_x=5.34, relative_y=-45.0):
                    Syllabic('begin')
                    Text('ver')
            with Note(default_x=206.56, default_y=-650.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=251.01, default_y=-645.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                    Slur(type='start', placement='above', number=2)
                with Lyric(number='1', default_x=1.44, default_y=-43.49, relative_x=1.44, relative_y=-45.0):
                    Syllabic('middle')
                    Text('ge')
            with Note(default_x=301.27, default_y=-640.6):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
                    Slur(type='stop', number=2)
            with Note(default_x=345.71, default_y=-635.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=12.1, default_y=-43.49, relative_x=2.63, relative_y=-45.0):
                    Syllabic('end')
                    Text('bens!')
        with Measure(number='65', width=373.44):
            with Note(default_x=31.13, default_y=-665.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('Drum')
            with Note(default_x=102.86, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('laßt')
            with Note(default_x=147.69, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=192.52, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=237.35, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=282.18, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-43.49, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=327.01, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-43.49, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='66', width=364.81):
            with Note(default_x=15.8, default_y=-630.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-43.49, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=86.55, default_y=-650.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=179.92, default_y=-650.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-43.49, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
        with Measure(number='67', width=606.48):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(492.74)
            with Note():
                Rest()
                Duration(2.0)
                Voice('1')
                Type('quarter')
            with Note(default_x=196.93, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('Laßt')
            with Note(default_x=264.92, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('uns')
            with Note(default_x=332.91, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
            with Note(default_x=400.91, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=468.9, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-45.0):
                    Syllabic('begin')
                    Text('fröh')
            with Note(default_x=536.89, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(1.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=10.67, default_y=-47.24, relative_x=1.69, relative_y=-45.0):
                    Syllabic('end')
                    Text('lich,')
        with Measure(number='68', width=567.96):
            with Note(default_x=16.92, default_y=-492.74):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=10.41, default_y=-47.24, relative_x=10.41, relative_y=-45.0):
                    Syllabic('single')
                    Text('froh')
                    Extend()
            with Note(default_x=129.21, default_y=-512.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=269.22, default_y=-512.74):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('half')
                Stem('down')
                with Lyric(number='1', default_x=13.03, default_y=-47.24, relative_x=2.99, relative_y=-45.0):
                    Syllabic('single')
                    Text('sein!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')