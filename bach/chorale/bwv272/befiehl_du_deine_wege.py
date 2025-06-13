with ScorePartwise(version='3.1'):
    with Work():
        WorkNumber('Beﬁehl du deine Wege')
    with Identification():
        Creator('J. s. Bach', type='composer')
        with Encoding():
            Supports(element='accidental', type='yes')
            Supports(element='beam', type='yes')
            Supports(element='print', attribute='new-page', type='yes', value='yes')
            Supports(element='print', attribute='new-system', type='yes', value='yes')
            Supports(element='stem', type='yes')
    with Defaults():
        with Scaling():
            Millimeters(7.572)
            Tenths(40.0)
        with PageLayout():
            PageHeight(1568.99)
            PageWidth(1109.19)
            with PageMargins(type='both'):
                LeftMargin(71.5796)
                RightMargin(71.5796)
                TopMargin(71.5796)
                BottomMargin(71.5796)
        WordFont(font_family='FreeSerif', font_size='10')
        LyricFont(font_family='Serif', font_size='10')
    with Credit(page=1):
        CreditType('composer')
        CreditWords('JSB', default_x=1037.61, default_y=1397.41, justify='right', valign='bottom', font_size='12')
    with Credit(page=1):
        CreditType('title')
        CreditWords('Befiehl du deine Wege', default_x=554.596, default_y=1497.41, justify='center', valign='top', font_size='24')
    with PartList():
        with PartGroup(type='start', number='1'):
            GroupSymbol('bracket')
        with ScorePart(id='P1'):
            PartName('Sopran')
            PartAbbreviation('S.')
            with ScoreInstrument(id='P1-I1'):
                InstrumentName('Sopran')
            MidiDevice(None, id='P1-I1', port=1)
            with MidiInstrument(id='P1-I1'):
                MidiChannel(1)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P2'):
            PartName('Alt')
            PartAbbreviation('A.')
            with ScoreInstrument(id='P2-I1'):
                InstrumentName('Alt')
            MidiDevice(None, id='P2-I1', port=1)
            with MidiInstrument(id='P2-I1'):
                MidiChannel(2)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P3'):
            PartName('Tenor')
            PartAbbreviation('T.')
            with ScoreInstrument(id='P3-I1'):
                InstrumentName('Tenor')
            MidiDevice(None, id='P3-I1', port=1)
            with MidiInstrument(id='P3-I1'):
                MidiChannel(3)
                MidiProgram(53)
                Volume(78.7402)
                Pan(0.0)
        with ScorePart(id='P4'):
            PartName('Bass')
            PartAbbreviation('B.')
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
        with Measure(number='0', implicit='yes', width=162.02):
            with Print():
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(82.19)
                        RightMargin(0.0)
                    TopSystemDistance(162.62)
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
                    with Metronome(parentheses='no', default_x=-37.31, relative_y=20.0):
                        BeatUnit('quarter')
                        PerMinute('72')
                Sound(tempo=72.0)
            with Note(default_x=101.08, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=-16.96, default_y=-45.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('1.Be')
            with Note(default_x=136.76, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='1', width=209.82):
            with Note(default_x=27.41, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('fiehl')
            with Note(default_x=66.06, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=113.4, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=157.7, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('ne')
        with Measure(number='2', width=155.81):
            with Note(default_x=25.93, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-45.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
            with Note(default_x=63.32, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.28, default_y=-45.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge,')
            with Note(default_x=110.23, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='3', width=209.7):
            with Note(default_x=18.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=61.35, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('dein')
            with Note(default_x=105.03, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=170.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('ze')
        with Measure(number='4', width=146.5):
            with Note(default_x=38.21, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=8.85, default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('kränkt,')
            with Note(default_x=88.03, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-45.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                    Extend()
            with Note(default_x=121.73, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=288.32):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.84)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=78.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('al')
            with Note(default_x=128.99, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ler')
            with Note(default_x=187.09, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('treu')
            with Note(default_x=238.08, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('sten')
        with Measure(number='6', width=214.43):
            with Note(default_x=33.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Pfle')
            with Note(default_x=113.65, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=163.24, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.34, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('des,')
        with Measure(number='7', width=247.81):
            with Note(default_x=18.03, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
            with Note(default_x=71.72, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('den')
            with Note(default_x=125.41, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Him')
            with Note(default_x=192.52, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('mel')
        with Measure(number='8', width=177.64):
            with Note(default_x=32.06, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=8.94, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('lenkt.')
            with Note(default_x=112.92, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Der')
        with Measure(number='9', width=350.79):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.84)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=90.82, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Wol')
            with Note(default_x=145.21, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ken,')
            with Note(default_x=213.2, default_y=-10.0):
                with Pitch():
                    Step('D')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Luft')
            with Note(default_x=247.2, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=281.2, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='10', width=250.98):
            with Note(default_x=12.0, default_y=-15.0):
                with Pitch():
                    Step('C')
                    Octave(5)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
                with Notations():
                    Slur(type='start', placement='above', number=1)
                with Lyric(number='1', default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Win')
            with Note(default_x=105.7, default_y=-20.0):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('down')
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=136.94, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('den')
            with Note(default_x=186.91, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('gibt')
        with Measure(number='11', width=326.43):
            with Note(default_x=39.15, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
            with Note(default_x=100.77, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.28, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge,')
            with Note(default_x=162.38, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('Lauf')
            with Note(default_x=224.0, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='12', width=928.2):
            with Print(new_system='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.84)
                        RightMargin(0.0)
                    SystemDistance(150.0)
            with Note(default_x=82.58, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.94, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Bahn,')
            with Note(default_x=555.84, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('der')
                    Extend()
            with Note(default_x=741.22, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='13', width=366.84):
            with Print(new_page='yes'):
                with SystemLayout():
                    with SystemMargins():
                        LeftMargin(37.84)
                        RightMargin(0.0)
                    TopSystemDistance(70.0)
            with Note(default_x=78.78, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('wird')
            with Note(default_x=145.54, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('auch')
            with Note(default_x=218.14, default_y=-25.0):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
            with Note(default_x=284.9, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
        with Measure(number='14', width=227.91):
            with Note(default_x=17.92, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Lyric(number='1', default_x=6.22, default_y=-45.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ﬁn')
            with Note(default_x=135.08, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.33, default_y=-45.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('den,')
            with Note(default_x=180.7, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('da')
        with Measure(number='15', width=238.33):
            with Note(default_x=18.03, default_y=-30.0):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('dein')
            with Note(default_x=84.72, default_y=-35.0):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Fuß')
            with Note(default_x=136.56, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
            with Note(default_x=178.04, default_y=-40.0):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-45.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('hen')
        with Measure(number='16', width=95.12):
            with Note(default_x=29.74, default_y=-45.0):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.94, default_y=-45.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('kann.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P2'):
        with Measure(number='0', implicit='yes', width=162.02):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(89.1)
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
            with Note(default_x=101.08, default_y=-174.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=-24.47, default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('2.\xa0Dem')
                    Extend()
            with Note(default_x=136.76, default_y=-179.1):
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
        with Measure(number='1', width=209.82):
            with Note(default_x=27.41, default_y=-174.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Her')
            with Note(default_x=66.06, default_y=-184.1):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.08, default_y=-60.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('ren')
            with Note(default_x=113.4, default_y=-189.1):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('musst')
            with Note(default_x=157.7, default_y=-174.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=185.05, default_y=-179.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=155.81):
            with Note(default_x=25.93, default_y=-179.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-60.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('trau')
            with Note(default_x=63.32, default_y=-179.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=4.77, default_y=-60.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
            with Note(default_x=110.23, default_y=-179.1):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('wenn')
        with Measure(number='3', width=209.7):
            with Note(default_x=18.03, default_y=-164.1):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text("dir's")
            with Note(default_x=61.35, default_y=-164.1):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
            with Note(default_x=105.03, default_y=-169.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('begin')
                    Text('wohl')
            with Note(default_x=170.54, default_y=-169.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.85, relative_y=-30.0):
                    Syllabic('middle')
                    Text('er')
        with Measure(number='4', width=146.5):
            with Note(default_x=38.21, default_y=-169.1):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.19, default_y=-60.85, relative_y=-30.0):
                    Syllabic('end')
                    Text('gehn;')
            with Note(default_x=88.03, default_y=-174.1):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-60.85, relative_y=-30.0):
                    Syllabic('single')
                    Text('auf')
                    Extend()
            with Note(default_x=121.73, default_y=-179.1):
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
        with Measure(number='5', width=288.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.79)
            with Note(default_x=78.78, default_y=-172.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein')
            with Note(default_x=128.99, default_y=-182.79):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Werk')
            with Note(default_x=187.09, default_y=-187.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('musst')
            with Note(default_x=238.08, default_y=-172.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
                    Extend()
            with Note(default_x=262.4, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=214.43):
            with Note(default_x=33.94, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-59.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('schau')
            with Note(default_x=113.65, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.24, default_y=-59.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('en,')
            with Note(default_x=163.24, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('wenn')
        with Measure(number='7', width=247.81):
            with Note(default_x=18.03, default_y=-162.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('dein')
            with Note(default_x=71.72, default_y=-162.79):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Werk')
            with Note(default_x=125.41, default_y=-167.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('soll')
            with Note(default_x=192.52, default_y=-167.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-59.39, relative_y=-30.0):
                    Syllabic('begin')
                    Text('be')
        with Measure(number='8', width=177.64):
            with Note(default_x=32.06, default_y=-167.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.41, default_y=-59.39, relative_y=-30.0):
                    Syllabic('end')
                    Text('stehn.')
            with Note(default_x=112.92, default_y=-167.79):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-59.39, relative_y=-30.0):
                    Syllabic('single')
                    Text('Mit')
                    Extend()
            with Note(default_x=144.48, default_y=-162.79):
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
        with Measure(number='9', width=350.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(87.79)
            with Note(default_x=90.82, default_y=-157.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Sor')
            with Note(default_x=145.21, default_y=-152.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('gen')
            with Note(default_x=213.2, default_y=-152.79):
                with Pitch():
                    Step('A')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=281.2, default_y=-157.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
        with Measure(number='10', width=250.98):
            with Note(default_x=12.0, default_y=-157.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(4.0)
                Tie(type='start')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='start')
                with Lyric(number='1', default_y=-50.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Grä')
            with Note(default_x=74.47, default_y=-162.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=105.7, default_y=-157.79):
                with Pitch():
                    Step('G')
                    Octave(4)
                Duration(2.0)
                Tie(type='stop')
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Tied(type='stop')
            with Note(default_x=136.94, default_y=-162.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('men')
            with Note(default_x=186.91, default_y=-162.79):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=218.14, default_y=-167.79):
                with Pitch():
                    Step('E')
                    Alter(-1.0)
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='11', width=326.43):
            with Note(default_x=39.15, default_y=-172.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('single')
                    Text('mit')
            with Note(default_x=100.77, default_y=-172.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('begin')
                    Text('selbst')
            with Note(default_x=162.38, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('middle')
                    Text('ei')
            with Note(default_x=224.0, default_y=-177.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.88, relative_y=-30.0):
                    Syllabic('end')
                    Text('gner')
        with Measure(number='12', width=928.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.22)
            with Note(default_x=82.58, default_y=-173.22):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-50.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Pein')
            with Note(default_x=555.84, default_y=-163.22):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-50.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('lässt')
        with Measure(number='13', width=366.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(88.95)
            with Note(default_x=78.78, default_y=-163.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('Gott')
            with Note(default_x=178.92, default_y=-168.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('sich')
            with Note(default_x=218.14, default_y=-163.95):
                with Pitch():
                    Step('F')
                    Octave(4)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('gar')
            with Note(default_x=318.28, default_y=-168.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('nichts')
        with Measure(number='14', width=227.91):
            with Note(default_x=18.28, default_y=-168.95):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-60.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('neh')
            with Note(default_x=48.17, default_y=-173.95):
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
            with Note(default_x=76.68, default_y=-173.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Tie(type='stop')
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Tied(type='stop')
            with Note(default_x=135.08, default_y=-178.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.02, default_y=-60.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('men,')
            with Note(default_x=180.7, default_y=-173.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('es')
        with Measure(number='15', width=238.33):
            with Note(default_x=18.03, default_y=-173.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('muss')
                    Extend()
            with Note(default_x=58.8, default_y=-178.95):
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
            with Note(default_x=84.72, default_y=-173.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
            with Note(default_x=136.56, default_y=-173.95):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('middle')
                    Text('be')
            with Note(default_x=178.04, default_y=-178.95):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-60.73, relative_y=-30.0):
                    Syllabic('end')
                    Text('ten')
        with Measure(number='16', width=95.12):
            with Note(default_x=29.74, default_y=-188.95):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.26, default_y=-60.73, relative_y=-30.0):
                    Syllabic('single')
                    Text('sein.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P3'):
        with Measure(number='0', implicit='yes', width=162.02):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(105.56)
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
            with Note(default_x=101.08, default_y=-299.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=-24.1, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('3.\xa0Dein')
                    Extend()
            with Note(default_x=136.76, default_y=-304.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='1', width=209.82):
            with Note(default_x=27.41, default_y=-299.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ew')
            with Note(default_x=66.06, default_y=-304.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ge')
            with Note(default_x=113.4, default_y=-309.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('Treu')
            with Note(default_x=157.7, default_y=-309.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
                    Extend()
            with Note(default_x=185.05, default_y=-314.66):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=155.81):
            with Note(default_x=25.93, default_y=-309.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Gna')
            with Note(default_x=63.32, default_y=-309.66):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=9.28, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('de,')
            with Note(default_x=110.23, default_y=-304.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('o')
        with Measure(number='3', width=209.7):
            with Note(default_x=18.03, default_y=-304.66):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Va')
            with Note(default_x=61.35, default_y=-289.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=9.11, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('ter,')
            with Note(default_x=105.03, default_y=-294.66):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('weiß')
                    Extend()
            with Note(default_x=142.45, default_y=-289.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=170.54, default_y=-284.66):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='4', width=146.5):
            with Note(default_x=38.21, default_y=-289.66):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.94, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('sieht')
            with Note(default_x=88.03, default_y=-299.66):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
                    Extend()
            with Note(default_x=121.73, default_y=-304.66):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='5', width=288.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(100.0)
            with Note(default_x=78.78, default_y=-292.79):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('gut')
            with Note(default_x=128.99, default_y=-297.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('sei')
            with Note(default_x=187.09, default_y=-302.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('o')
            with Note(default_x=238.08, default_y=-302.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('der')
            with Note(default_x=262.4, default_y=-307.79):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=214.43):
            with Note(default_x=33.94, default_y=-302.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=6.22, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('scha')
            with Note(default_x=113.65, default_y=-302.79):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('de')
            with Note(default_x=163.24, default_y=-297.79):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('dem')
        with Measure(number='7', width=247.81):
            with Note(default_x=18.03, default_y=-297.79):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('men')
            with Note(default_x=71.72, default_y=-282.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('middle')
                    Text('schli')
            with Note(default_x=125.41, default_y=-287.79):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('chen')
            with Note(default_x=158.96, default_y=-282.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=192.52, default_y=-277.79):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('begin')
                    Text('Ge')
        with Measure(number='8', width=177.64):
            with Note(default_x=32.06, default_y=-282.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.69, default_y=-47.79, relative_y=-30.0):
                    Syllabic('end')
                    Text('blüt;')
            with Note(default_x=112.92, default_y=-282.79):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.79, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='9', width=350.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(91.49)
            with Note(default_x=90.82, default_y=-269.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
            with Note(default_x=145.21, default_y=-264.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=213.2, default_y=-269.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('dann')
            with Note(default_x=281.2, default_y=-269.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('er')
        with Measure(number='10', width=250.98):
            with Note(default_x=12.0, default_y=-274.28):
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
                with Lyric(number='1', default_y=-47.18, relative_y=-30.0):
                    Syllabic('middle')
                    Text('le')
            with Note(default_x=43.23, default_y=-264.28):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=74.47, default_y=-269.28):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.7, default_y=-274.28):
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
            with Note(default_x=136.94, default_y=-274.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=9.49, default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen,')
            with Note(default_x=186.91, default_y=-274.28):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('das')
        with Measure(number='11', width=326.43):
            with Note(default_x=39.15, default_y=-279.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('treibst')
            with Note(default_x=100.77, default_y=-284.28):
                with Pitch():
                    Step('A')
                    Alter(-1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('flat')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('single')
                    Text('du')
            with Note(default_x=162.38, default_y=-289.28):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-47.18, relative_y=-30.0):
                    Syllabic('begin')
                    Text('star')
            with Note(default_x=268.81, default_y=-284.28):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
                Beam('begin', number=2)
                with Lyric(number='1', default_y=-47.18, relative_y=-30.0):
                    Syllabic('end')
                    Text('ker')
                    Extend()
            with Note(default_x=296.82, default_y=-279.28):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(3)
                Duration(1.0)
                Voice('1')
                Type('16th')
                Stem('up')
                Beam('end', number=1)
                Beam('end', number=2)
        with Measure(number='12', width=928.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(93.49)
            with Note(default_x=82.58, default_y=-281.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=8.86, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('Held,')
            with Note(default_x=555.84, default_y=-281.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-40.0, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
        with Measure(number='13', width=366.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(106.1)
            with Note(default_x=78.78, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('bringst')
            with Note(default_x=145.54, default_y=-285.05):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('zum')
            with Note(default_x=178.92, default_y=-290.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=218.14, default_y=-290.05):
                with Pitch():
                    Step('C')
                    Octave(4)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Stand')
            with Note(default_x=284.9, default_y=-285.05):
                with Pitch():
                    Step('D')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('und')
            with Note(default_x=318.28, default_y=-280.05):
                with Pitch():
                    Step('E')
                    Octave(4)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='14', width=227.91):
            with Note(default_x=18.28, default_y=-300.05):
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
                with Lyric(number='1', default_y=-51.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('We')
            with Note(default_x=48.17, default_y=-305.05):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=76.68, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=106.58, default_y=-295.05):
                with Pitch():
                    Step('B')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.08, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', default_y=2.15, relative_y=10.0)
                with Lyric(number='1', default_x=9.49, default_y=-51.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('sen,')
            with Note(default_x=180.7, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('was')
        with Measure(number='15', width=238.33):
            with Note(default_x=18.03, default_y=-305.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('dei')
            with Note(default_x=84.72, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('nem')
            with Note(default_x=136.56, default_y=-300.05):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('single')
                    Text('Rat')
            with Note(default_x=203.96, default_y=-305.05):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                with Lyric(number='1', default_x=6.58, default_y=-51.44, relative_y=-30.0):
                    Syllabic('begin')
                    Text('ge')
        with Measure(number='16', width=95.12):
            with Note(default_x=29.74, default_y=-310.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
                with Lyric(number='1', default_x=8.76, default_y=-51.44, relative_y=-30.0):
                    Syllabic('end')
                    Text('fällt.')
            with Barline(location='right'):
                BarStyle('light-heavy')
    with Part(id='P4'):
        with Measure(number='0', implicit='yes', width=162.02):
            with Print():
                with StaffLayout(number=1):
                    StaffDistance(88.39)
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
            with Note(default_x=101.08, default_y=-413.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=136.76, default_y=-418.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='1', width=209.82):
            with Note(default_x=27.41, default_y=-423.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=84.92, default_y=-428.05):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=113.4, default_y=-423.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=140.06, default_y=-428.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=157.7, default_y=-433.05):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=185.05, default_y=-428.05):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='2', width=155.81):
            with Note(default_x=25.93, default_y=-448.05):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=63.32, default_y=-448.05):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=110.23, default_y=-418.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='3', width=209.7):
            with Note(default_x=18.03, default_y=-423.05):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=61.35, default_y=-423.05):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=105.03, default_y=-418.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=170.54, default_y=-453.05):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='4', width=146.5):
            with Note(default_x=38.21, default_y=-438.05):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=88.03, default_y=-413.05):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=121.73, default_y=-418.05):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='5', width=288.32):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.63)
            with Note(default_x=78.78, default_y=-418.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(6.0)
                Voice('1')
                Type('quarter')
                Dot()
                Stem('down')
            with Note(default_x=153.31, default_y=-423.42):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
            with Note(default_x=187.09, default_y=-418.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=213.76, default_y=-423.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=238.08, default_y=-428.42):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=262.4, default_y=-423.42):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='6', width=214.43):
            with Note(default_x=33.94, default_y=-443.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(8.0)
                Voice('1')
                Type('half')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=113.65, default_y=-443.42):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=163.24, default_y=-413.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='7', width=247.81):
            with Note(default_x=18.03, default_y=-418.42):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=71.72, default_y=-418.42):
                with Pitch():
                    Step('D')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=125.41, default_y=-413.42):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=192.52, default_y=-448.42):
                with Pitch():
                    Step('E')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='8', width=177.64):
            with Note(default_x=32.06, default_y=-433.42):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=112.92, default_y=-398.42):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='9', width=350.79):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(90.4)
            with Note(default_x=90.82, default_y=-389.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=145.21, default_y=-389.67):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=179.21, default_y=-394.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=213.2, default_y=-399.67):
                with Pitch():
                    Step('F')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('down')
            with Note(default_x=281.2, default_y=-394.67):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=315.19, default_y=-399.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('down')
                Beam('end', number=1)
        with Measure(number='10', width=250.98):
            with Note(default_x=12.0, default_y=-404.67):
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
            with Note(default_x=43.23, default_y=-414.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=74.47, default_y=-409.67):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('continue', number=1)
            with Note(default_x=105.7, default_y=-404.67):
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
            with Note(default_x=136.94, default_y=-399.67):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=186.91, default_y=-434.67):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='11', width=326.43):
            with Note(default_x=39.15, default_y=-419.67):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=100.77, default_y=-419.67):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('natural')
                Stem('up')
            with Note(default_x=162.38, default_y=-414.67):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
            with Note(default_x=224.0, default_y=-449.67):
                with Pitch():
                    Step('C')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='12', width=928.2):
            with Print(new_system='yes'):
                with StaffLayout(number=1):
                    StaffDistance(83.22)
            with Note(default_x=82.58, default_y=-424.92):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=555.84, default_y=-404.92):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Accidental('sharp')
                Stem('up')
        with Measure(number='13', width=366.84):
            with Print(new_page='yes'):
                with StaffLayout(number=1):
                    StaffDistance(94.66)
            with Note(default_x=78.78, default_y=-429.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=112.16, default_y=-434.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=145.54, default_y=-439.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=178.92, default_y=-434.7):
                with Pitch():
                    Step('C')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=218.14, default_y=-454.7):
                with Pitch():
                    Step('F')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=251.52, default_y=-444.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('end', number=1)
            with Note(default_x=284.9, default_y=-439.7):
                with Pitch():
                    Step('B')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('natural')
                Stem('up')
                Beam('begin', number=1)
            with Note(default_x=318.28, default_y=-434.7):
                with Pitch():
                    Step('C')
                    Alter(1.0)
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
        with Measure(number='14', width=227.91):
            with Note(default_x=18.28, default_y=-429.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('begin', number=1)
                with Notations():
                    Slur(type='start', placement='below', number=1)
            with Note(default_x=48.17, default_y=-439.7):
                with Pitch():
                    Step('B')
                    Alter(-1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('flat')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=76.68, default_y=-444.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('up')
                Beam('continue', number=1)
            with Note(default_x=106.58, default_y=-449.7):
                with Pitch():
                    Step('G')
                    Alter(1.0)
                    Octave(2)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Accidental('sharp')
                Stem('up')
                Beam('end', number=1)
                with Notations():
                    Slur(type='stop', number=1)
            with Note(default_x=135.08, default_y=-444.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Note(default_x=180.7, default_y=-429.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
        with Measure(number='15', width=238.33):
            with Note(default_x=18.03, default_y=-424.7):
                with Pitch():
                    Step('E')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=84.72, default_y=-419.7):
                with Pitch():
                    Step('F')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('begin', number=1)
            with Note(default_x=110.64, default_y=-414.7):
                with Pitch():
                    Step('G')
                    Octave(3)
                Duration(2.0)
                Voice('1')
                Type('eighth')
                Stem('down')
                Beam('end', number=1)
            with Note(default_x=136.56, default_y=-409.7):
                with Pitch():
                    Step('A')
                    Octave(3)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('down')
            with Note(default_x=178.04, default_y=-444.7):
                with Pitch():
                    Step('A')
                    Octave(2)
                Duration(4.0)
                Voice('1')
                Type('quarter')
                Stem('up')
        with Measure(number='16', width=95.12):
            with Note(default_x=29.74, default_y=-429.7):
                with Pitch():
                    Step('D')
                    Octave(3)
                Duration(12.0)
                Voice('1')
                Type('half')
                Dot()
                Stem('down')
                with Notations():
                    Fermata(None, type='upright', relative_y=10.0)
            with Barline(location='right'):
                BarStyle('light-heavy')