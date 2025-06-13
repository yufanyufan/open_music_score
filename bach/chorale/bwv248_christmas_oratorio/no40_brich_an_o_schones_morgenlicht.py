with ScorePartwise(version='3.1'):
    with Work():
        WorkTitle('Brich an, o schönes Morgenlicht')
    with Identification():
        Creator('J. S. Bach', type='composer')
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
        CreditWords('Brich an, o schönes Morgenlicht', default_x=671.547, default_y=1834.59, justify='center', valign='top', font_size='24')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('J. S. Bach', default_x=1279.15, default_y=1644.03, justify='right', valign='bottom', font_size='12')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Soprano', print_object='no')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Soprano')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alto', print_object='no')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alto')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor', print_object='no')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass', print_object='no')
            with ScoreInstrument(id='P4-I1'):
                InstrumentName('Bass')
            MidiDevice(None, id='P4-I1', port=1)
            with MidiInstrument(id='P4-I1'):
                MidiChannel(4)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        PartGroup(type='stop', number='1')
    with Part(id='P1'):
        with Measure(number='0', implicit='yes', width=184.22):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.41)
                        RightMargin(0.0)
                    TopSystemDistance(260.55)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Direction(placement='above'):
                with DirectionType():
                    with Metronome(parentheses='no', default_x=-41.11, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('70')
                Sound(tempo=70.0)
            with Note(default_x=104.88, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='1', width=277.08):
            with Note(default_x=20.3, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=84.01, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ten')
            with Note(default_x=147.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schö')
                with Lyric(number='2', default_y=-73.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('volk,')
                    Extend()
            with Note(default_x=179.91, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.77, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='2', width=306.78):
            with Note(default_x=28.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=105.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('cke')
            with Note(default_x=166.69, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.01, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
                with Lyric(number='2', default_x=8.94, default_y=-73.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=228.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
        with Measure(number='3', width=271.65):
            with Note(default_x=20.98, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=83.25, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
            with Note(default_x=145.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=207.78, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='4', width=169.07):
            with Note(default_x=15.44, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
                with Lyric(number='2', default_x=6.22, default_y=-73.21, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=109.69, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.38, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen!')
                with Lyric(number='2', default_x=6.58, default_y=-73.21, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=132.85):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.41)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=78.78, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='6', width=222.2):
            with Note(default_x=18.5, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=66.67, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=116.53, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=182.07, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='7', width=222.26):
            with Note(default_x=23.69, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=48.43, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=73.16, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=122.64, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=162.22, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
        with Measure(number='8', width=233.01):
            with Note(default_x=16.24, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=64.4, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=120.79, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
                    Extend()
            with Note(default_x=156.59, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.26, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=208.79):
            with Note(default_x=25.94, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=76.29, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=116.57, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.23, default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein,')
            with Note(default_x=156.84, default_y=-5.0):
                with Pitch():
                    Step('E')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='10', width=189.69):
            with Note(default_x=15.34, default_y=0.0):
                with Pitch():
                    Step('F')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('zu')
            with Note(default_x=60.81, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=102.46, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=144.1, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
        with Measure(number='11', width=473.07):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(6.41)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=87.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=289.63, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=370.45, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='12', width=425.68):
            with Note(default_x=16.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=118.17, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=220.14, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=322.11, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
                    Extend()
            with Note(default_x=373.1, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='13', width=310.05):
            with Note(default_x=23.1, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=224.28, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=184.22):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(93.83)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
            with Note(default_x=104.88, default_y=-183.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='1', width=277.08):
            with Note(default_x=20.3, default_y=-183.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.0, default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=84.01, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ten')
            with Note(default_x=147.72, default_y=-183.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schö')
                with Lyric(number='2', default_y=-86.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('volk,')
                    Extend()
            with Note(default_x=179.91, default_y=-178.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.77, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='2', width=306.78):
            with Note(default_x=28.2, default_y=-178.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
                with Lyric(number='2', default_y=-86.14, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=66.67, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=105.14, default_y=-168.83):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('cke')
            with Note(default_x=166.69, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.01, default_y=-60.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
                with Lyric(number='2', default_x=8.94, default_y=-86.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=228.24, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
        with Measure(number='3', width=271.65):
            with Note(default_x=20.98, default_y=-178.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
            with Note(default_x=83.25, default_y=-183.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.16, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
                with Lyric(number='2', default_y=-86.14, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                    Extend()
            with Note(default_x=114.38, default_y=-178.83):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.52, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=207.78, default_y=-168.83):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='4', width=169.07):
            with Note(default_x=15.8, default_y=-168.83):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.16, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
                with Lyric(number='2', default_y=-86.14, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=57.53, default_y=-173.83):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=109.69, default_y=-183.83):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.38, default_y=-60.16, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen!')
                with Lyric(number='2', default_x=6.58, default_y=-86.14, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=132.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(70.99)
            with Note(default_x=78.78, default_y=-150.99):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                    Extend()
            with Note(default_x=105.01, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=222.2):
            with Note(default_x=18.5, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=90.75, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('sess')
            with Note(default_x=116.53, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=149.3, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=182.07, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='7', width=222.26):
            with Note(default_x=23.69, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=73.16, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=122.64, default_y=-155.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=162.22, default_y=-155.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=195.92, default_y=-160.99):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=233.01):
            with Note(default_x=16.24, default_y=-155.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=64.4, default_y=-155.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=120.79, default_y=-155.99):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
                    Extend()
            with Note(default_x=156.59, default_y=-150.99):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=183.26, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=207.34, default_y=-150.99):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='9', width=208.79):
            with Note(default_x=25.94, default_y=-150.99):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=51.12, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=76.29, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=116.57, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.23, default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein,')
            with Note(default_x=156.84, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='10', width=189.69):
            with Note(default_x=15.34, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('zu')
                    Extend()
            with Note(default_x=36.17, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.81, default_y=-135.99):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.54, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=102.46, default_y=-135.99):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=123.28, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=144.1, default_y=-140.99):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-60.54, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
                    Extend()
            with Note(default_x=164.93, default_y=-145.99):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=473.07):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(67.6)
            with Note(default_x=87.22, default_y=-142.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-63.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=289.63, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=370.45, default_y=-142.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-63.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=420.96, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='12', width=425.68):
            with Note(default_x=16.2, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=118.17, default_y=-147.6):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=220.14, default_y=-142.6):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-63.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=271.13, default_y=-137.6):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=322.11, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-63.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='13', width=310.05):
            with Note(default_x=23.46, default_y=-152.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-63.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=148.11, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.28, default_y=-157.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-63.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=184.22):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(114.25)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('G')
                    Line(2)
                    ClefOctaveChange(-1)
            with Note(default_x=104.88, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('Du')
        with Measure(number='1', width=277.08):
            with Note(default_x=20.3, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_x=0.45, default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
                    Extend()
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Hir')
            with Note(default_x=52.16, default_y=-308.07):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=115.87, default_y=-303.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ten')
            with Note(default_x=147.72, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-44.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schö')
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('volk,')
                    Extend()
            with Note(default_x=179.91, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=211.77, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='2', width=306.78):
            with Note(default_x=28.2, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schre')
            with Note(default_x=105.14, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('cke')
            with Note(default_x=166.69, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.01, default_y=-44.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
                with Lyric(number='2', default_x=8.94, default_y=-70.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('nicht,')
            with Note(default_x=228.24, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('weil')
                    Extend()
            with Note(default_x=266.71, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='3', width=271.65):
            with Note(default_x=20.98, default_y=-323.07):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                    Extend()
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('dir')
                    Extend()
            with Note(default_x=52.11, default_y=-318.07):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.25, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-44.96, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('single')
                    Text('die')
                    Extend()
            with Note(default_x=114.38, default_y=-308.07):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.52, default_y=-303.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('En')
            with Note(default_x=207.78, default_y=-303.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-44.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('gel')
        with Measure(number='4', width=169.07):
            with Note(default_x=15.8, default_y=-303.07):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-44.96, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
                with Lyric(number='2', default_y=-70.93, relative_y=-30.0):
                    Syllabic('begin')
                    Text('sa')
            with Note(default_x=83.61, default_y=-308.07):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=109.69, default_y=-313.07):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.38, default_y=-44.96, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen!')
                with Lyric(number='2', default_x=6.58, default_y=-70.93, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=132.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.3)
            with Note(default_x=78.78, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
                    Extend()
            with Note(default_x=105.01, default_y=-248.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='6', width=222.2):
            with Note(default_x=18.5, default_y=-243.29):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=42.58, default_y=-248.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.67, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=116.53, default_y=-248.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=182.07, default_y=-243.29):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='7', width=222.26):
            with Note(default_x=23.69, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=73.16, default_y=-248.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=97.9, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=122.64, default_y=-258.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=162.22, default_y=-273.29):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=195.92, default_y=-268.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=233.01):
            with Note(default_x=16.24, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=40.32, default_y=-258.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=64.4, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
                    Extend()
            with Note(default_x=88.48, default_y=-248.29):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=120.79, default_y=-258.29):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
            with Note(default_x=183.26, default_y=-258.29):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=208.79):
            with Note(default_x=25.94, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=76.29, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=116.57, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.23, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein,')
            with Note(default_x=156.84, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
        with Measure(number='10', width=189.69):
            with Note(default_x=15.34, default_y=-253.29):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('zu')
            with Note(default_x=60.81, default_y=-238.29):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=102.46, default_y=-273.29):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-47.24, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=123.28, default_y=-268.29):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=144.1, default_y=-263.29):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.24, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
        with Measure(number='11', width=473.07):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(92.0)
            with Note(default_x=87.58, default_y=-249.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-53.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=138.09, default_y=-254.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=188.6, default_y=-249.6):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=239.11, default_y=-259.6):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=289.63, default_y=-254.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=370.45, default_y=-254.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-53.89, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='12', width=425.68):
            with Note(default_x=16.2, default_y=-254.6):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-53.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=67.19, default_y=-259.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=118.17, default_y=-259.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
                    Extend()
            with Note(default_x=169.16, default_y=-264.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=220.14, default_y=-264.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=271.13, default_y=-269.6):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=322.11, default_y=-274.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-53.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='13', width=310.05):
            with Note(default_x=23.46, default_y=-274.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-53.89, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=78.86, default_y=-279.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('continue', number=1)
                Beam('begin', number=2)
            with Note(default_x=113.48, default_y=-284.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
            with Note(default_x=148.11, default_y=-279.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.28, default_y=-264.6):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-53.89, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='0', implicit='yes', width=184.22):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(108.89)
            with Attributes():
                Divisions(4.0)
                with Key():
                    Fifths(-1)
                with Time(symbol='common'):
                    Beats('4')
                    BeatType('4')
                with Clef():
                    Sign('F')
                    Line(4)
            with Note(default_x=104.88, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('Brich')
                    Extend()
            with Note(default_x=143.75, default_y=-451.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='1', width=277.08):
            with Note(default_x=20.3, default_y=-456.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.0, default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('an,')
            with Note(default_x=84.01, default_y=-461.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
            with Note(default_x=147.72, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schö')
            with Note(default_x=211.77, default_y=-451.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('nes')
                    Extend()
            with Note(default_x=243.62, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='2', width=306.78):
            with Note(default_x=28.2, default_y=-441.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-58.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Mor')
            with Note(default_x=105.14, default_y=-476.97):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.38, relative_y=-30.0):
                    Syllabic('middle')
                    Text('gen')
            with Note(default_x=166.69, default_y=-461.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.01, default_y=-58.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('licht,')
            with Note(default_x=228.24, default_y=-461.97):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='3', width=271.65):
            with Note(default_x=20.98, default_y=-456.97):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('lass')
                    Extend()
            with Note(default_x=52.11, default_y=-451.97):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=83.25, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=114.38, default_y=-466.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=145.52, default_y=-431.97):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=176.65, default_y=-436.97):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=207.78, default_y=-441.97):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
                    Extend()
            with Note(default_x=238.92, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='4', width=169.07):
            with Note(default_x=15.8, default_y=-426.97):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-58.38, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ta')
            with Note(default_x=57.53, default_y=-461.97):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=109.69, default_y=-446.97):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.38, default_y=-58.38, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen!')
            with Barline(location='right'):
                BarStyle('light-heavy')
                Repeat(direction='backward')
        with Measure(number='5', width=132.85):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(86.02)
            with Note(default_x=78.78, default_y=-389.31):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('dass')
        with Measure(number='6', width=222.2):
            with Note(default_x=18.5, default_y=-354.31):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('die')
            with Note(default_x=42.58, default_y=-359.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=66.67, default_y=-364.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('ses')
            with Note(default_x=116.53, default_y=-369.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schwa')
            with Note(default_x=182.07, default_y=-389.31):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('che')
        with Measure(number='7', width=222.26):
            with Note(default_x=23.69, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Knä')
            with Note(default_x=73.16, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=122.64, default_y=-404.31):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('lein')
            with Note(default_x=162.22, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
                    Extend()
            with Note(default_x=195.92, default_y=-379.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='8', width=233.01):
            with Note(default_x=16.24, default_y=-374.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('un')
            with Note(default_x=64.4, default_y=-374.31):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('ser')
            with Note(default_x=120.79, default_y=-369.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('Trost')
            with Note(default_x=183.26, default_y=-369.31):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=208.79):
            with Note(default_x=25.94, default_y=-364.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Freu')
            with Note(default_x=76.29, default_y=-399.31):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=116.57, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.23, default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein,')
            with Note(default_x=156.84, default_y=-354.31):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('da')
            with Note(default_x=182.02, default_y=-359.31):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='10', width=189.69):
            with Note(default_x=15.34, default_y=-364.31):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('zu')
                    Extend()
            with Note(default_x=36.17, default_y=-369.31):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=60.81, default_y=-374.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
                    Extend()
            with Note(default_x=81.63, default_y=-379.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=102.46, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sa')
            with Note(default_x=123.28, default_y=-379.31):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=144.1, default_y=-374.31):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.86, relative_y=-30.0):
                    Syllabic('end')
                    Text('tan')
                    Extend()
            with Note(default_x=164.93, default_y=-384.31):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
        with Measure(number='11', width=473.07):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(82.0)
            with Note(default_x=87.58, default_y=-391.6):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('zwin')
            with Note(default_x=138.09, default_y=-396.6):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=188.6, default_y=-391.6):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=239.11, default_y=-401.6):
                with Pitch():
                    Step('G')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=289.63, default_y=-386.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=370.45, default_y=-396.6):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.02, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='12', width=425.68):
            with Note(default_x=16.2, default_y=-391.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('letzt')
            with Note(default_x=118.17, default_y=-386.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('lich')
            with Note(default_x=220.14, default_y=-381.6):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-51.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Frie')
            with Note(default_x=271.13, default_y=-376.6):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=322.11, default_y=-371.6):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
        with Measure(number='13', width=310.05):
            with Note(default_x=23.46, default_y=-391.6):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='start', placement='below', number=1)
                with Lyric(number='1', default_y=-51.02, relative_y=-30.0):
                    Syllabic('begin')
                    Text('brin')
            with Note(default_x=148.11, default_y=-386.6):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=224.28, default_y=-406.6):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=8.71, default_y=-51.02, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen.')
            with Barline(location='right'):
                BarStyle('light-heavy')